# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Conjunto de importações        
import requests
import json        

#caminho base para requisitar a Graph API
GET ='/v2.5/me HTTP/1.1'
base_url = "https://graph.facebook.com/"
#objeto para a requisição. representa o seu perfil pessoal no Facebook
objeto = "/me"
#preencha aqui com o valor do seu token de acesso
access_token = "EAAiP22c2BtEBADAKYSbiy91RdGlUIh8mPfRy8IkqXeEg6wplrekLUheWG7FoJ5lAkuWqgxy0AxQZCVNkQQpIQkR9xqQfIpUSMZA6TS0gIzsyLYyKFe34NhLkos99Bwo3WrUrVASzeDzvD9Raxvu2Q49ZAbhIO8kaWSZAk6vbqJwZBcZBmVh4hgA4JzDmcDRKDmMfnwNByZAyeo20QIluzSTLWZBGfgreYZCtcfQjlEsaKvVLfKbpXs2sV"

#campos da pesquisa
campos = "id,name,likes,picture"
#campos = "id,name,likes"
campos = "id,name,posts,likes"
campos = "likes"
#campos = "reactions"
#campos = "commets"

#definição da URL de requisição
#cada %s será substituído por uma variável listada entre parênteses, na ordem em que foram definidas
url = '%s%s?access_token=%s' % (base_url, objeto, access_token) 

#envia a requisição
#recebe a resposta no formato JSON
dados = requests.get(url).json()
#apresenta a resposta identada
print (json.dumps(dados, indent=4))
