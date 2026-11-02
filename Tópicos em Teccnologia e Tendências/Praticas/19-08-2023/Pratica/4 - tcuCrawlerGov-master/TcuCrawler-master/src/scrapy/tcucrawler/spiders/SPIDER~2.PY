# DATAPREV
# Autor: Ricardo Roberto de Lima
# Projeto: SSA - Strategy Source Analytics - Captura de Dados
# ComprasGovMaster - Capturando e passando os dados para os arquivos *.csv.

from scrapy.selector import Selector

import scrapy
import json
import re
import csv


class Extracao(scrapy.Spider):
    # Nome do spider: Deve ser usado para chamar no terminal
    # Exemplo: scrapy crawl <nome>
    #          scrapy crawl <nome> -a <param=value>
    name = "tcucrawler-extracao"

    # Endpoints nos quais o spider deve fazer a extração
    endpoints = None

    # Define as configurações para esse spider (output, etc...)
    custom_settings = {
        "ITEM_PIPELINES" : {
            'tcucrawler.pipelines.CSVExtracaoPipeline': 300,
        },
        
        "CONCURRENT_REQUESTS" : 12,
        "DOWNLOAD_DELAY" : 3,

        "COOKIES_ENABLED" : False,
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }


    def __init__(self, endpoints=None, *args, **kwargs):
        # Chama o construtor da classe base (Spider)
        super(Extracao, self).__init__(*args, **kwargs)

        # Salva o nome do arquivo no qual contém os endpoints a serem extraidos
        self.endpoints = endpoints


    def start_requests(self):
        # Abre o arquivo com a lista de endereços a serem extraídos (endpoints.csv)
		# Importante para realizar a extração de múltiplas fontes da API de dados simultaneamente
        with open(self.endpoints, "r") as file:
            # Carrega o leitor de CSV com o arquivo
            reader = csv.reader(file)

            # Ignora o cabeçalho/header
            next(reader)

            for line in reader:
                # Obtêm o módulo (grupo), método (tabela), url e a quantidade de registros
                # É esperado que o CSV endpoints siga esse formato
                base, tipo, es_type = line

                # Ignora o endpoint se não tiver registro nenhum
                # Isso significa que não vai extrair tabelas que não contem nenhum dado
                count = 1
                if int(count) == 0:
                    continue

                # Adiciona o nome do método e do módulo da API/Endpoint
                # Esses serão usados para definir o arquivo correto para salvar os dados extraídos
                meta = {"_module_" : base, "_method_" : tipo}

                # Define o tempo máximo de espera pela requisição
                # Como a API é beta e tem limitações, melhor definir um timeout maior
                meta["download_timeout"] = 600

                # Faz a requisição para a API, para extrair os dados
                for i in range(0, int(count), 500):
                    # Monta a URL para a próxima requisição/offset
                    next_page = "{}?offset={}".format(es_type, i)

                    # Faz o request para a próxima offset
                    yield scrapy.Request(next_page, callback=self.parse, meta=meta)

    
    def parse(self, response):
        # Desserializa o JSON, fazendo o parse todo o conteúdo para um dict
        content = json.loads(response.text)

        # Obtêm os registros retornados pela API do governo
        # Os registros são armazenados em uma chave "_embedded", e dentro dela sempre tem um array
        # com os registros retornados da API, porém sempre com um nome diferente.
        # Então, obtemos primeiro o nome dessa chave, assim sendo possível de obter os registros
        keyname = list(content["_embedded"].keys())[0]
        result = content["_embedded"][keyname]
        
        # Obtêm o offset dessa resposta da API
        offset = 0 if "offset" not in content else content["offset"]

        for item in result:
            # Essa tabela não tem uma ID explícita?
            if "id" not in item:
                # Uma das respostas da API é o _links, que contém relações desse registro
                # com outras tabelas da API (exemplo: Pregões->Termos, Pregões->Declarações, etc.)
                # Essa chave também guarda "self", que contém a referência desse registro na API
                # Com essa referência/ID é possível fazer todas essas ligações, então o salvamos
                # Verifica se o _links existe/"self" está presente (onde tem o ID) e o adiciona
                if "_links" in item and "self" in item["_links"]:
                    # A ID é armazenada no link para a referência do registro, então obtemos
                    # o valor (código/ID) no final do link, e para isso dividimos a string
                    item["id"] = item["_links"]["self"]["href"].split("/")[-1]
            
            # Remove a chave de links, se existir
            item.pop("_links")

            # Adiciona um campo para manter a offset/página de onde esse registro foi obtido
            # Isso pode ser útil para ver até onde o crawler conseguiu buscar dados da API
            item["offset"] = offset

            # Adiciona o nome do arquivo ao item, seguindo o modelo de módulo e método
            # Esse campo é usado para o spider saber para onde esse item vai ser exportado (CSV)
            item["item_filename"] = "{}.{}".format(response.meta["_module_"], response.meta["_method_"])

            # Retorna (como generator) o registro obtido, para o mesmo ser exportado
            yield item