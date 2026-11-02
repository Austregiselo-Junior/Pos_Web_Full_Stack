# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados da pessoa como: id, name, first_name, last_name, gender, website, cover
import requests
import json        

base_url = "https://graph.facebook.com/"
objeto = "me"
#access_token = "329484294160599|RICnpAHDI6MEYxmx19Vb9aqKSDg"
access_token = "EAAiP22c2BtEBADAKYSbiy91RdGlUIh8mPfRy8IkqXeEg6wplrekLUheWG7FoJ5lAkuWqgxy0AxQZCVNkQQpIQkR9xqQfIpUSMZA6TS0gIzsyLYyKFe34NhLkos99Bwo3WrUrVASzeDzvD9Raxvu2Q49ZAbhIO8kaWSZAk6vbqJwZBcZBmVh4hgA4JzDmcDRKDmMfnwNByZAyeo20QIluzSTLWZBGfgreYZCtcfQjlEsaKvVLfKbpXs2sV"
# access_token = "EAAaiYyc2LgMBAHdUU5GZCLWAfnllNJH8ZChWCI5SGiXecb0T9YnVsqZBurqCYZCCZC2VxhyrHna0XZBeZB3x2K2IZCNJ9tXVe8dMJZAmkCKzESYMVuhgswc9ZB18qiCrhOtEEjnI07fXSSWNtjKZCNbPNTUB1EMK78dQaUUks2kZAwZA7cJ5FtH3uzU5U70jeAP8htZAj1H1iimAfKhT5AZC64aIjinTZCitsx7BRZBPPmNLTkZABxFxh204tJQnZAZC"
#Definição dos campos que iremos coletar
campos = "id,name,first_name,last_name,gender,website, cover"
#A URL agora terá a variável campos
url = "%s%s?fields=%s&access_token=%s" % (base_url, objeto, campos, access_token)

#Envia a requisição
#Armazena a resposta na variável dados
dados = requests.get(url).json()
#Apresenta a resposta no formato JSON identadamente
print (json.dumps(dados, indent=4))
