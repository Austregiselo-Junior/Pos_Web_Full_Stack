#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Disciplina: Gestão do Conhecimento e Big Data
Professor: Ricardo Roberto de Lima
Aluno: Nivaldo Mariano de Carvalho Junior

Projeto PaaS com Bottle
"""

from bottle import default_app, template, request, post, get
from bottle import run
from sklearn.naive_bayes import GaussianNB
import joblib
import nltk

# caminho da pasta do projeto no servidor
PASTA_PROJETO = "/home/projetonmcj/mysite/"


@get("/")
def index():
    # renderiza a página inicial do projeto
    return template(PASTA_PROJETO + "index.html")


@get("/projeto_mamiferos")
def mamiferos_get():
    # renderiza o formulário de classificação de mamíferos
    return template(PASTA_PROJETO + "forms/form_mamifero.html", animal="-", classificacao="-", probabilidade="-")


@post("/projeto_mamiferos")
def mamiferos_post():
    # obtêm valores informados no formulário
    animal = request.forms.get('animal')
    sangue = int(request.forms.get('sangue'))
    bota_ovo = int(request.forms.get('bota_ovo'))
    voa = int(request.forms.get('voa'))
    mora_agua = int(request.forms.get('mora_agua'))

    # carrega o modelo
    modelo_nb = GaussianNB()
    modelo_nb = joblib.load(PASTA_PROJETO + "models/model_mamifero.pkl")

    # executa a classificação
    res = modelo_nb.predict([[sangue, bota_ovo, voa, mora_agua]])

    # encontra o valor da confidência
    prb = modelo_nb.predict_proba([[sangue, bota_ovo, voa, mora_agua]])

    if res == 1:
        clf = "Mamífero"
    elif res == 0:
        clf = "Não mamífero"
    else:
        clf = "Indefinido"

    # renderiza o template com os resultados
    return template(PASTA_PROJETO + "forms/form_mamifero.html", animal=animal, classificacao=clf, probabilidade=prb)


@get("/projeto_credito")
def credito_get():
    # renderiza o formulário de classificação de crédito
    return template(PASTA_PROJETO + "forms/form_credito.html", risco="-", renda="-", probabilidade="-")


@post("/projeto_credito")
def credito_post():
    # obtêm valores informados no formulário
    pessoa = request.forms.get('pessoa')
    renda = float(request.forms.get('renda'))
    credito = int(request.forms.get('credito'))
    divida = int(request.forms.get('divida'))
    garantias = int(request.forms.get('garantias'))

    # carrega o modelo
    modelo_nb = GaussianNB()
    modelo_nb = joblib.load(PASTA_PROJETO + "models/model_credito.pkl")

    # executa a classificação
    res = modelo_nb.predict([[renda, credito, divida, garantias]])

    # encontra o valor da confidência
    prb = modelo_nb.predict_proba([[renda, credito, divida, garantias]])

    if res == 1:
        clf = "Alto"
    elif res == 0:
        clf = "Medio"
    else:
        clf = "Indefinido"

    # renderiza o template com os resultados
    return template(PASTA_PROJETO + "forms/form_credito.html", risco=clf, renda=renda, probabilidade=prb)


@get("/projeto_nltk")
def linguagem_get():
    # renderiza o formulário de classificação de texto
    return template(PASTA_PROJETO + "forms/form_nltk.html", classificacao="-", classes="-")


@post("/projeto_nltk")
def linguagem_post():
    """
    pacotes instalados: averaged_perceptron_tagger, city_database, floresta, 
    comparative_sentences, large_grammars, mac_morpho, machado, opinion_lexicon,
    sample_grammars, spanish_grammars, twitter_samples, unicode_samples, rslp,
    names, omw, qc, stopwords, udhr2, wordnet, ieer
    """
    # realiza o download dos arquivos da library
    # nltk.download()

    # faz a leitura do texto
    texto = str(request.forms.get('texto')).lower().strip()

    # separa o texto por palavras e realiza stemming
    stemmer = nltk.stem.RSLPStemmer()
    texto_stem = []

    for palavra in texto.split():
        texto_stem.append(str(stemmer.stem(palavra)))

    # carrega o modelo
    unique_words = joblib.load(
        PASTA_PROJETO + "models/model_ntlk_uniquewords.pkl")
    classifier = joblib.load(
        PASTA_PROJETO + "models/model_nltk_classifier.pkl")

    # prepara texto para classificação, obtendo as características
    docmnt = set(texto_stem)
    caract = {}

    for palavras in unique_words:
        caract['%s' % palavras] = (palavras in docmnt)

    # executa a classificação
    clasf = classifier.classify(caract)
    distr = classifier.prob_classify(caract)
    reslt = []

    for classe in distr.samples():
        reslt.append("%s: %f" % (classe, (distr.prob(classe) * 100)))

    reslt = " - ".join(reslt)

    # renderiza o template com os resultados
    return template(PASTA_PROJETO + "forms/form_nltk.html", classificacao=clasf, classes=reslt)


# executa a aplicação bottle
application = default_app()

# necessário para executar localmente
run(application, host="localhost", port=80)
