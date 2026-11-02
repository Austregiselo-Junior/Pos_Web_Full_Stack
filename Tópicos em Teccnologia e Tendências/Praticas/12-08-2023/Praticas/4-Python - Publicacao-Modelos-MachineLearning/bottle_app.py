#Autor: Ricardo Roberto de Lima - 2018 -> projeto de bottle
#Conjunto de importacoes
from bottle import default_app, template, request, post, get
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

#Definição das possíveis rotas para a função de callback

@get('/')
@get('/form/')
def index():
     #Definição de valores iniciais para as expressões animal, classificação e probabilidade
     return template('/home/ricardorobertolima/mysite/Formulario.html', animal = "-", classificacao = "-", probabilidade = "-")

#Definição da rota e função de callback
@post('/form/')
def index_resposta():
    #Pega os valores informados no formulário e atribui a variaveis locais
    animal = request.forms.get('animal')
    sangue = request.forms.get('sangue')
    bota_ovo = request.forms.get('bota_ovo')
    voa = request.forms.get('voa')
    mora_agua = request.forms.get('mora_agua')

    modelo_NB = GaussianNB()
    #Carrega o modelo gerado
    modelo_NB = joblib.load('/home/ricardorobertolima/mysite/modelo_mamifero_MNB.pkl')
    #Executa a classificação
    res = modelo_NB.predict([[int(sangue), int(bota_ovo), int(voa), int(mora_agua)]])

    #Encontra o valor da confidência
    probabilidade = modelo_NB.predict_proba([[int(sangue), int(bota_ovo), int(voa), int(mora_agua)]])

    if res == 1:
        classificacao = "Mamífero"
    elif res == 0:
        classificacao = "Não Mamífero"
    else:
        classificacao = "Indefinido"

    #Renderiza o template com os valores passados como argumento
    return template('/home/ricardorobertolima/mysite/Formulario.html', animal = animal, classificacao = classificacao, probabilidade = probabilidade)
    #return template('/home/ricardorobertolima/mysite/Formulario.html', animal = animal, classificacao = classificacao)

application = default_app()
