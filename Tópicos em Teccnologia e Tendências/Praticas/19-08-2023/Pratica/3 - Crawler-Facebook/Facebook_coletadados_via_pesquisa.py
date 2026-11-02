# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados via pesquisa genérica do face..

#Conjunto de importações
import requests
import json        

base_url = "https://graph.facebook.com/search"

q = "java python ruby"
#tipo = "page"
#tipo = "event"
#tipo = "group"
tipo = "page"

#O objeto receberá o ID da página 
access_token = '329484294160599|RICnpAHDI6MEYxmx19Vb9aqKSDg'

#access_token = 'EAAErqgpQANcBAAZBlSQi0MyEAl2WX0ZBTOkvXiA2iqcVZBZB7CDaZCqShvFieAsuvQx1O9WKK3XixqHpoFpSYCIj74Pd22OudDa6Pqams0Dv7ZAKXoi94gOo2CenoLQwBg1x0wY430KIIPObrpAVFkbXDx09IILNXD8CmZB2uzNyZB2w4pGvjrZAL2ZBS1uELyp7oZD'

#acess_token = 'EAAbh5iKgawkBALoA4EZCuPZArV3obrEAYknu3T458pk5F9ZCIWMpZBXm6xy1J9R1SilZANwtDyfgJXDPFtmyqnguVDuLG7ZCb31VsrGFDsHnwqe69zYaad2gt0LlrfLO9XYZAiPPHpZC0pASiZCVEtOnfefVRQyOuZB4ZBAnKBPms83WXudI11ZAWZByZBZAZA7SNujgz3snIglK95Jrtzoxlu1E8wCvX9uMIp8UxGu0tUB6vOlRpTl6dCR8sQqA'


url = "%s?q=%s&type=%s&access_token=%s" % (base_url, q, tipo, access_token) 

#Envia a requisição

#Armazena a resposta na variável dados
dados = requests.get(url).json()

#Apresenta a resposta no formato JSON identadamente
print (json.dumps(dados, indent=4))
