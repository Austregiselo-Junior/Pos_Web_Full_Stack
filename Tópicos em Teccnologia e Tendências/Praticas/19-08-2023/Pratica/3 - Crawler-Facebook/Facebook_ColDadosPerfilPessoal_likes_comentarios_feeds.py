# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados da pessoa como: curtidas (likes), reações (reactions), comentários (comments), publicações (posts) e (shares).
import requests
import json        

base_url = "https://graph.facebook.com/"
#Variável para definir a versão que queremos requisitar
versao = "v2.8/"
#objeto = "1858205874418972"
objeto = "250335092151706"
#access_token = "329484294160599|RICnpAHDI6MEYxmx19Vb9aqKSDg"
access_token = "EAAiP22c2BtEBADAKYSbiy91RdGlUIh8mPfRy8IkqXeEg6wplrekLUheWG7FoJ5lAkuWqgxy0AxQZCVNkQQpIQkR9xqQfIpUSMZA6TS0gIzsyLYyKFe34NhLkos99Bwo3WrUrVASzeDzvD9Raxvu2Q49ZAbhIO8kaWSZAk6vbqJwZBcZBmVh4hgA4JzDmcDRKDmMfnwNByZAyeo20QIluzSTLWZBGfgreYZCtcfQjlEsaKvVLfKbpXs2sV"
#access_token = "1867396603588099|u3qpoHRQntixOjxLQ-J4rEFAvrY"
#Definição dos campos que iremos coletar
#campos = "id,name,likes"
#campos = "id,name,posts"
campos = "likes"
#campos = "reactions"
#campos = "commets"
campos = "sharedposts"

#A URL agora terá a variável campos
url = "%s%s?fields=%s&access_token=%s" % (base_url, objeto, campos, access_token)

#Envia a requisição
#Armazena a resposta na variável dados
dados = requests.get(url).json()
#Apresenta a resposta no formato JSON identadamente
print (json.dumps(dados, indent=4))

