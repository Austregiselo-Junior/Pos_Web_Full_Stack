# -*- coding: utf-8 -*-
# DATAPREV
# Autor: Ricardo Roberto de Lima
# Projeto: SSA - Strategy Source Analytics - Captura de Dados
# ComprasGovMaster - Capturando e passando os dados para os arquivos *.csv.
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

import json

""" Pipeline usada para persistir os dados extraídos da API do governo em CSVs distintos """
class CSVExtracaoPipeline(object):

    def open_spider(self, spider):
        # Inicializa o dict de CSV Exporters
        self.exporters = {}
    
    def close_spider(self, spider):
        # Finaliza cada exporter usado ao concluir a extração
        for exporter in self.exporters.values():
            exporter.finish_exporting()

    def _exporter_for_item(self, item):
        """ Obtêm o Exporter correto para o item a ser exportado. """
        """ Ver: https://doc.scrapy.org/en/latest/topics/exporters.html?highlight=CSV#using-item-exporters """

        # Obtêm o nome do arquivo no qual deve ser salvo o item, e o remove do item
        filename = item["item_filename"]

        # O nome do arquivo não está nos exporters?
        if filename not in self.exporters:
            # Cria um arquivo para o exporter
            file = open(filename + ".csv", "w+b")

            # Cria o exporter para esse arquivo
            exporter = CsvItemExporter(file, delimiter="\t")

            # Inicia o exporter (deixa-o pronto para salvar registros extraídos)
            exporter.start_exporting()
            
            # Adiciona esse exporter na lista de exporters
            self.exporters[filename] = exporter
        
        # Retorna o exporter específico para o item
        return self.exporters[filename]

    def process_item(self, item, spider):
        # Exporter é uma classe específica para a persistência de dados extraídos,
        # para formatos comuns (como CSV). Cada item da API a ser extraído terá seu próprio exporter,
        # já que extraímos dados de vários endpoints da API diferentes, demandando vários CSVs
        exporter = self._exporter_for_item(item)

        # Persiste o item no arquivo CSV correto usando o Exporter
        exporter.export_item(item)

        return item


""" Pipeline usada para persistir os endpoints da API do governo em um único CSV """
class CSVEndpointsPipeline(object):
    
    def open_spider(self, spider):
        # Cria o arquivo de saída dos endpoints
        self.file = open("endpoints.csv", "wb")

        # Inicia o exporter
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()


    def process_item(self, item, spider):
        # Envia o item para o CSV
        self.exporter.export_item(item)
        return item


    def close_spider(self, spider):
        # Finaliza o processo
        self.exporter.finish_exporting()