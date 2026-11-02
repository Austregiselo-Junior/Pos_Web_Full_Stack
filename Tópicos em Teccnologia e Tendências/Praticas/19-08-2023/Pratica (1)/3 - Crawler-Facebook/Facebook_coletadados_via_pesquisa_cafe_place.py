# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados via pesquisa genérica do face..

#Conjunto de importações
import requests
import json        

base_url = "https://graph.facebook.com/search"

q = "cafe"
tipo = "place"
centro = "-15.77972,-47.92972"
distancia = "50000"

#O objeto receberá o ID da página 
access_token = "EAAiP22c2BtEBADAKYSbiy91RdGlUIh8mPfRy8IkqXeEg6wplrekLUheWG7FoJ5lAkuWqgxy0AxQZCVNkQQpIQkR9xqQfIpUSMZA6TS0gIzsyLYyKFe34NhLkos99Bwo3WrUrVASzeDzvD9Raxvu2Q49ZAbhIO8kaWSZAk6vbqJwZBcZBmVh4hgA4JzDmcDRKDmMfnwNByZAyeo20QIluzSTLWZBGfgreYZCtcfQjlEsaKvVLfKbpXs2sV"

url = "%s?q=%s&type=%s&center=%s&distance=%s&access_token=%s" % (base_url, q, tipo, centro, distancia, access_token)

#Envia a requisição

#Armazena a resposta na variável dados
dados = requests.get(url).json()

#Salvar os dados coletados no arquivo facebook_data.json
with open("facebook_data_ricardo_RRL.json", mode="a") as meu_arquivo:
    json.dump(dados, meu_arquivo, indent=4) 

#Apresenta a resposta no formato JSON identadamente
print (json.dumps(dados, indent=4))
