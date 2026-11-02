# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados da Página do NerflixBrasil..

#Conjunto de importações
import requests
import json        

base_url = "https://graph.facebook.com/"
#O objeto receberá o ID da página 
objeto = "NetflixBrasil"
#objeto = "1372184469505009"
#access_token = 'EAAErqgpQANcBAAZBlSQi0MyEAl2WX0ZBTOkvXiA2iqcVZBZB7CDaZCqShvFieAsuvQx1O9WKK3XixqHpoFpSYCIj74Pd22OudDa6Pqams0Dv7ZAKXoi94gOo2CenoLQwBg1x0wY430KIIPObrpAVFkbXDx09IILNXD8CmZB2uzNyZB2w4pGvjrZAL2ZBS1uELyp7oZD'
access_token = "EAAiP22c2BtEBADAKYSbiy91RdGlUIh8mPfRy8IkqXeEg6wplrekLUheWG7FoJ5lAkuWqgxy0AxQZCVNkQQpIQkR9xqQfIpUSMZA6TS0gIzsyLYyKFe34NhLkos99Bwo3WrUrVASzeDzvD9Raxvu2Q49ZAbhIO8kaWSZAk6vbqJwZBcZBmVh4hgA4JzDmcDRKDmMfnwNByZAyeo20QIluzSTLWZBGfgreYZCtcfQjlEsaKvVLfKbpXs2sV"
#campos = 'fan_count'
#campos = "posts.limit(5)"
campos = "likes"

url = '%s%s?access_token=%s' % (base_url, objeto, campos, access_token) 

#Envia a requisição
#Armazena a resposta na variável dados
dados = requests.get(url).json()
#Apresenta a resposta no formato JSON identadamente
print (json.dumps(dados, indent=4))
