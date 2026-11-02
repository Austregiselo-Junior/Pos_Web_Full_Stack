# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados Facebook e Gravar em Arquivo JSon.

import requests
import json

base_url = "https://graph.facebook.com/"
objeto = "1372184469505009"
campos = "reactions"

access_token = "EAAiP22c2BtEBADAKYSbiy91RdGlUIh8mPfRy8IkqXeEg6wplrekLUheWG7FoJ5lAkuWqgxy0AxQZCVNkQQpIQkR9xqQfIpUSMZA6TS0gIzsyLYyKFe34NhLkos99Bwo3WrUrVASzeDzvD9Raxvu2Q49ZAbhIO8kaWSZAk6vbqJwZBcZBmVh4hgA4JzDmcDRKDmMfnwNByZAyeo20QIluzSTLWZBGfgreYZCtcfQjlEsaKvVLfKbpXs2sV"
url = "%s?fields=%s&access_token=%s" % (base_url, campos, access_token)

dados = requests.get(url).json()

#Salvar os dados coletados no arquivo facebook_data.json
with open("facebook_dataRRL.json", mode="a") as meu_arquivo:
    json.dump(dados, meu_arquivo, indent=4) 
