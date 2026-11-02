# DATAPREV
# Autor: Ricardo Roberto de Lima
# Projeto: SSA - Strategy Source Analytics - Captura de Dados
# ComprasGovMaster - Capturando e passando os dados para os arquivos *.csv.

from scrapy.selector import Selector

import scrapy
import json


class Endpoints(scrapy.Spider):

    # Nome do spider: Deve ser usado para chamar no terminal
    # Exemplo: scrapy crawl <nome>
    #          scrapy crawl <nome> -a <param=value>
    name = "tcucrawler-endpoints"

    # Define as configurações para esse spider (output, etc...)
    custom_settings = {
        "ITEM_PIPELINES" : {
            'tcucrawler.pipelines.CSVEndpointsPipeline': 300,
        }
    }
    

    def errback(self, failure):
        # Callback para exibir no LOG o erro na requisição
        # Evita que o script falhe caso não consiga acessar (Exception)
        self.logger.error(repr(failure))
        pass


    def is_valid_url(self, url):
        # URLs que tem {} precisam de parâmetros, pois são de consulta
        # Obtemos apenas endpoints sem consulta, então as que tem {} não são 'válidas'
        return "{" not in url and "}" not in url


    def start_requests(self):
        # URL base para a API de Endpoints/Documentação Automática
        url = "https://pesquisa.apps.tcu.gov.br/#/pesquisa/integrada"

        # Realiza a requisição para a API, para fazer o parse dos módulos da mesma
        yield scrapy.Request(url=url, callback=self.parse_modules)
    

    def parse_modules(self, response):
        # Extrai a lista de módulos da API (links)
        modules = response.selector.xpath('//a[@class="titulo_modulo"]').extract()

        for module in modules:
            # Obtêm o URL relativo para o módulo e cria o URL absoluto
            module_link = Selector(text=module).xpath('//@href').extract_first()
            module_link = response.urljoin(module_link)

            # Extrai o path atual do módulo, que serão usadas para construir URLs de método (JSON)
            module_path = module_link.split("/")[-2]

            # Cada módulo contém uma documentação em formato específico (HTML ou JSON)
            # Então precisamos fazer o parse dos métodos do endpoint de acordo com o formato
            if "api-docs" in module_link:
                yield scrapy.Request(url=module_link, 
                                     callback=self.parse_methods_json, 
                                     meta={"module_path" : module_path})
            else:
                yield scrapy.Request(url=module_link, 
                                     callback=self.parse_methods_html, 
                                     meta={"module_path" : module_path})
    

    def parse_methods_json(self, response):
        # Carrega o conteúdo do JSON
        content = json.loads(response.text)

        # Obtêm os caminhos/paths dos métodos
        paths = [item["path"] for item in content["apis"]]

        for path in paths:
            # Se tem uma referência para o path atual, então os próximos paths são endpoints de dados
            if "resourcePath" in content:
                # Como vamos salvar a URL para o recurso (e não a URL de documentação),
                # Criamos o próximo request com a URL absoluta para o recurso, usando o path do módulo
                url = "https://pesquisa.apps.tcu.gov.br/#/pesquisa/integrada/" + response.meta["module_path"] + path + ".json"

                # Guarda no 'meta' o nome da tabela/endpoint
                response.meta["method_name"] = path.split("/")[-1]

                # Caso seja um path de consulta única, ignore
                # Isso é útil para evitar 500 Internal Server Errors
                if not self.is_valid_url(path):
                    continue

                # Define timeout e a quantidade de vezes pra tentar
                # Alguns endpoints da API são inválidos então definir isso evita o script 'travar'
                response.meta["download_timeout"] = 10
                response.meta["max_retry_times"] = 2

                # Fazemos uma nova requisição à API para fazer o parse do recurso/endpoint
                yield scrapy.Request(url=url, 
                                     callback=self.parse, 
                                     meta=response.meta,
                                     errback=self.errback)
            else:
                # Precisamos criar uma URL absoluta para o path relativo retornado pelo Swagger
                url = "{}{}".format(response.url, path)

                # Para cada caminho de método encontrado, faz uma nova busca por mais caminhos
                yield scrapy.Request(url=url, callback=self.parse_methods_json, meta=response.meta)


    def parse_methods_html(self, response):
        # Dessa documentação, extrai a tabela de métodos de consultas básicas
        table = response.selector.xpath('//table[1]/tbody/tr').extract()

        for item in table:
            # Obtêm o path para o método
            path = Selector(text=item).xpath('//td/a/@href').extract_first()

            # Guarda no 'meta' o nome/caminho da tabela/endpoint
            response.meta["module_path"] = path.split("/")[0]
            response.meta["method_name"] = path.split("/")[2].replace(".html", "")

            # Cria a URL absoluta para o método/recurso JSON
            url = "https://pesquisa.apps.tcu.gov.br/#/pesquisa/integrada/" + path.replace(".html", ".json")

            # Caso seja um path de consulta única, ignore
            # Isso é útil para evitar 500 Internal Server Errors
            if not self.is_valid_url(url):
                continue

            # Define timeout e a quantidade de vezes pra tentar
            # Alguns endpoints da API são inválidos então definir isso evita o script 'travar'
            response.meta["download_timeout"] = 10
            response.meta["max_retry_times"] = 2
            
            # Fazemos uma nova requisição à API para fazer o parse do recurso/endpoint
            yield scrapy.Request(url=url, 
                                 callback=self.parse, 
                                 meta=response.meta,
                                 errback=self.errback)


    def parse(self, response):
        # Carrega o conteúdo do JSON recebido
        content = json.loads(response.text)

        # Retorna as informações do endpoint
        yield {
            "module" : response.meta["module_path"],
            "method" : response.meta["method_name"],
            "url"    : response.url,
            "count"  : content["count"] if "count" in content else 0
        }