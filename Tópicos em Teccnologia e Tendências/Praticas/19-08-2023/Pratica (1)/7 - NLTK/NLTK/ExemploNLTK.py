#   Autor: Ricardo Roberto de Lima
#   Arquivo com as Informações sobre instalação e configuração do pacote NLTK e NUMPY.
# - Vá para o Diretório do Python na pasta Script e digite -
# - easy_install.exe nltk
# - easy_install.exe numpy

import numpy as np

import nltk
# - nltk.download()

texto_Portugues = 'Ricardo Roberto de Lima'
texto_Ingles = 'Mr. Green killed Colonel Mustard in the study  with the candlestick. Mr. Green is very nice friend'
print(texto_Ingles.split('.'))

# conseguiu quebrar em várias frases o texto acima.
# frases = nltk.tokenize.sent_tokenize(texto_Ingles)
# print(frases)

# tokens = nltk.word_tokenize(texto_Ingles)
# print(tokens)

# classes = nltk.pos_tag(tokens)
# print(classes)

# acessar o link para ver a tabela com as principais siglas de NLTK classe gramatical.
# http://https://cs.nyu.edu/grishman/jet/guide/PennPOS.html

# entidades = nltk.chunk.ne_chunk(classes)
# print(entidades)

# No resultado será apresentado algumas informações sobre  os dados existentes em cada classe.
# Detecção de Entidades. Retorna as informações - Pessoa, Organização, Etc.






