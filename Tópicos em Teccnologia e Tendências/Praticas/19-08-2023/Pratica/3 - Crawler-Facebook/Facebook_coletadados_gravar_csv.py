# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados Facebook e Gravar em Arquivo CSV.

import requests
import json
import csv

base_url = "https://graph.facebook.com/"
objeto = "1372184469505009"
campos = "likes"
access_token = "EAAiP22c2BtEBADAKYSbiy91RdGlUIh8mPfRy8IkqXeEg6wplrekLUheWG7FoJ5lAkuWqgxy0AxQZCVNkQQpIQkR9xqQfIpUSMZA6TS0gIzsyLYyKFe34NhLkos99Bwo3WrUrVASzeDzvD9Raxvu2Q49ZAbhIO8kaWSZAk6vbqJwZBcZBmVh4hgA4JzDmcDRKDmMfnwNByZAyeo20QIluzSTLWZBGfgreYZCtcfQjlEsaKvVLfKbpXs2sV"
#access_token = "EAAErqgpQANcBAAZBlSQi0MyEAl2WX0ZBTOkvXiA2iqcVZBZB7CDaZCqShvFieAsuvQx1O9WKK3XixqHpoFpSYCIj74Pd22OudDa6Pqams0Dv7ZAKXoi94gOo2CenoLQwBg1x0wY430KIIPObrpAVFkbXDx09IILNXD8CmZB2uzNyZB2w4pGvjrZAL2ZBS1uELyp7oZD"
url = "%s?fields=%s&access_token=%s" % (base_url, campos, access_token)

dados = requests.get(url).json()

#Salvar os dados coletados no arquivo facebook_data.csv
meu_arquivo = open('facebook1_data2022.csv', mode='a', encoding='utf-8')
writer = csv.writer(meu_arquivo)
for dado in dados['name']['data']:
    writer.writerow([dado['id'], dado['name'], dado['type']])
meu_arquivo.close()
