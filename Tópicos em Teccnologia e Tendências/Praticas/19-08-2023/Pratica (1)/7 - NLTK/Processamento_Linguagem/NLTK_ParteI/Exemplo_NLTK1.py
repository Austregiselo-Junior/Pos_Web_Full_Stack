import nltk
#import numpy as np
#nltk.download()

Texto =  'Mr. Green is portrayed as a plump, pompous looking business man with grey hair. On the box, he is wearing a grayish suit with a green tie, while on his card, his suit is brown.'
#Texto = 'estou contente com o resultado do teste que fiz no dia de ontem'
print(Texto.split('.'))

Frases = nltk.tokenize.sent_tokenize(Texto)
print(Frases)

tokens = nltk.word_tokenize(Texto)
print(tokens)

classes = nltk.pos_tag(tokens)
print(classes)

entidades = nltk.chunk.ne_chunk(classes)
print(entidades)

