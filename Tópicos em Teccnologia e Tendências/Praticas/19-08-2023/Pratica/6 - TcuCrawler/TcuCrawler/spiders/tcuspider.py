# DATAPREV
# Autor: Ricardo Roberto de Lima
# Projeto: SSA - Strategy Source Analytics - Captura de Dados
# TCUCrawLer - Capturando e passando os dados para o ElasticSearch.

import csv

import scrapy
import json

class TCUSpider(scrapy.Spider):

    # Nome do Spider (como deverá ser invocado via Terminal)
    name = "tcuspider"

    # Aqui é definido as configurações específicas para ESSE spider
    # Deve ser alterado AQUI as configurações do spider, não no 'settings.py's
    custom_settings = {
        # Define a pipeline onde os itens devem ir para serem persistidos
        "ITEM_PIPELINES" : {
            # Descomente essa linha para usar a saída em CSV
            #'TcuCrawler.pipelines.CSVCustomPipeline' : 300,

            # Descomente essa linha para usar a saída em ElasticSearch
            #'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 500
            'TcuCrawler.pipelines.ESCustomPipeline' : 500,
        },

        # ----- Configurações do ElasticSearchPipeline -----
        # ElasticSearch: IP/Porta do Servidor
        "ELASTICSEARCH_SERVERS" : ['localhost:9200'],

        # ElasticSearch: Nome do Index onde deve salvar
        # O padrão é `scrapy`, mas deve ser modificado dinamicamente pelo Pipeline
        "ELASTICSEARCH_INDEX" : "scrapy",

        # ElasticSearch: Nome do Type onde deve salvar
        # O padrão é `item`, mas deve ser modificado dinamicamente pelo Pipeline
        "ELASTICSEARCH_TYPE" : "item",

        # Usuário e Senha do Servidor ElasticSearch
        #"ELASTICSEARCH_USERNAME" : "",
        #"ELASTICSEARCH_PASSWORD" : "",
        # ----- Configurações do ElasticSearchPipeline -----

        # Número de requisições simultâneas/concorrentes
        "CONCURRENT_REQUESTS" : 2,

        # Intervalo em segundos entre cada chamada à API
        "DOWNLOAD_DELAY" : 3,

        # Nível de log [CRITICAL, ERROR, WARNING, INFO, DEBUG]
        "LOG_LEVEL" : "INFO",

        # Extensão para mudar dinamicamente a velocidade de carga no servidor dependendo da latência
        "AUTOTHROTTLE_ENABLED" : True,

        # User-agent (identifica-se como browser obtendo os dados)
        "USER_AGENT" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    }

    # Endereço URL base da API do ComprasNET
    # Considerando que o URL não muda, apenas os métodos/bases
    #url = "https://contas.tcu.gov.br/buscaTextual2RS/rest/base/"
    url = "https://pesquisa.apps.tcu.gov.br/#/pesquisa/"

    # Nome do arquivo que contém a lista de endpoints/bases da API
    # Será preenchido em tempo de execução ao iniciar o script (via __init__)
    arquivo_endpoints = None

    # Quantidade de registros disponível 

    def __init__(self, endpoints=None, *args, **kwargs):
        # Inicializa o Spider
        super(TCUSpider, self).__init__(*args, **kwargs)

        # Salva o nome do arquivo que contém os endpoints a serem obtidos
        self.arquivo_endpoints = endpoints

    
    def start_requests(self):
        with open(self.arquivo_endpoints, "r") as file:
            # Leitura do arquivo com os endpoints a serem extraídos
            reader = csv.reader(file)
            next(reader)

            for line in reader:
                # Obtêm o nome da base de dados e o tipo de extração
                base, tipo, es_type  = line

                # Cria a URL de acesso a essa base
                url = "{}{}/{}".format(self.url, base, tipo)

                # Adiciona o nome da base de dados que está sendo obtida nessa requisição
                # O `type` onde será salvo os dados também é obtido do CSV de Endpoints
                meta = {
                    "__origem__"  : base, 
                    "__destino__" : es_type
                }

                # Inicia o crawling dos dados na API
                yield scrapy.Request(url=url, callback=self.start, meta=meta)


    def start(self, response):
        # Passa a resposta da API para JSON
        content = json.loads(response.text)

        # Define de onde devemos começar a obter os dados
        # Aqui que pode ser modificado de que posição iniciar o crawling, caso necessário
        start = 0

        # Define quantos registros por vez/por requisição devem ser obtidos da API
        step = 50

        # Nessa primeira requisição, obtemos a quantidade de registros disponíveis na base
        # Aqui pode ser modificado para obter apenas uma quantidade X de registros dessa base
        stop = int(content["quantidadeEncontrada"])

        for index in range(start, stop, step):
            # Formata a URL para obter a quantidade de registros por vez
            url = "{}?quantidade={}&inicio={}".format(response.url, step, index)

            # Adiciona informações de metadados à requisição
            meta = {
                "__origem__"  : response.meta["__origem__"], 
                "__destino__" : response.meta["__destino__"],
                "__offset__"  : str(index)
            }

            # Realiza a requisição à API
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)
        

    
    def parse(self, response):
        # Passa a resposta da API para um JSON
        content = json.loads(response.text)

        for item in content["documentos"]:
            # Para cada item, adicione o nome da base de onde foi obtido
            item["__origem__"] = response.meta["__origem__"]

            # Adiciona o nome da base de destino (onde será salvo no ElasticSearch)
            item["__destino__"] = response.meta["__destino__"]

            # Adiciona o 'início' da requisição (página/offset)
            # Útil para debugar se chegou todos os dados da API de fato
            item["__offset__"] = response.meta["__offset__"]

            # Retorne o item, realizado o parse do mesmo
            yield item