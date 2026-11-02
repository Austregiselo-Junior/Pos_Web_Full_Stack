# -*- coding: utf-8 -*-
# DATAPREV
# Autor: Ricardo Roberto de Lima
# Projeto: SSA - Strategy Source Analytics - Captura de Dados
# TCUCrawLer - Capturando e passando os dados para o ElasticSearch.
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

from scrapy.exporters import CsvItemExporter
from scrapyelasticsearch import scrapyelasticsearch

import hashlib
import logging
import types

# Pipeline para persistir dados em CSVs distintos
class CSVCustomPipeline(object):
    
    def open_spider(self, spider):
        # Cria um dicionário de exporters que irão os itens obtidos
        # Cada item dentro do `exporters` é um objeto de escrita CSV
        self.exporters = {}
    
    def close_spider(self, spider):
        # Ao fechar o spider, fecha todos os arquivos CSVs usados
        for exporter in self.exporters.values():
            exporter.finish_exporting()
    
    def _exporter_for_item(self, item):
        # Obtenha o nome do arquivo CSV para onde deve ir o item
        filename = item["__destino__"]

        # Se o nome do arquivo ainda não tiver nos exporters,
        # Cria um objeto de escrita para esse arquivo
        if filename not in self.exporters:
            file     = open(filename + ".csv", "w+b")
            exporter = CsvItemExporter(file, delimiter="\t")
            exporter.start_exporting()
            self.exporters[filename] = exporter
        
        # Retorna o objeto de escrita para o arquivo
        return self.exporters[filename]

    def process_item(self, item, spider):
        # Obtêm o objeto de escrita (exporter) para o item
        exporter = self._exporter_for_item(item)

        # Exporta o item para o arquivo correto
        exporter.export_item(item)

        # Retorna o item processado
        return item

class ESCustomPipeline(scrapyelasticsearch.ElasticSearchPipeline):

    def index_item(self, item):
        # Obtêm o nome do INDEX onde deve ser salvo o item
        index_name = item["__destino__"]

        # Obtêm e adiciona o formato de data que deve ser usado pelo exporter
        index_suffix_format = self.settings.get('ELASTICSEARCH_INDEX_DATE_FORMAT', None)
        if index_suffix_format:
            index_name += "-" + datetime.strftime(datetime.now(), index_suffix_format)
        
        # Dict de `actions` que o Pipeline deve tomar para o item
        index_action = {
            # INDEX onde deve ser salvo o item
            '_index'  : index_name,

            # TYPE onde deve ser salvo o item (obtêm dependendo de que item é)
            '_type'   : item["__destino__"],
            
            # SOURCE do item (conteúdo)
            '_source' : dict(item) 
        }

        # Foi definida alguma UNIQUE KEY para uso com o spider?
        if self.settings["ELASTICSEARCH_UNIQ_KEY"] is not None:
            # Obtêm a UNIQUE KEY do item
            item_unique_key = item[self.settings["ELASTICSEARCH_UNIQ_KEY"]]

            # Obtêm a UNIQUE KEY no ES4
            # pylint: disable=E1101
            unique_key = self.get_unique_key(item_unique_key)

            # Cria a hash para o item (ID)
            item_id = hashlib.sha1(unique_key).hexdigest()

            # Adiciona no dict de actions o ID do item
            index_action["_id"] = item_id

            logging.debug('Generated unique key %s' % item_id)
        
        # Adiciona o item no buffer [bulk insert?]
        self.items_buffer.append(index_action)

        # Se o buffer está cheio, envia os itens para o ElasticSearch
        if len(self.items_buffer) >= self.settings.get('ELASTICSEARCH_BUFFER_LENGTH', 500):
            self.send_items()
            self.items_buffer = []


# ------------
class TcucrawlerPipeline(object):
    def process_item(self, item, spider):
        return item
