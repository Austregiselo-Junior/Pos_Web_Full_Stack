# Projeto 3 - Modelagem de Tópicos do Noticiário Financeiro

# Versão 1 - Voting

# Imports
import numpy as np
from nltk.corpus import stopwords
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Carregando os dados
noticias = load_files('dados', encoding = 'utf-8', decode_error = 'replace')

# Separando variáveis de entrada e saída
X = noticias.data
y = noticias.target

# Lista de stop words
my_stop_words = set(stopwords.words('english'))

# Divisão em treino e teste (70/30)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.30, random_state = 75)

# Vetorização
vectorizer = TfidfVectorizer(norm = None, stop_words = my_stop_words, max_features = 1000, decode_error = "ignore")

# Aplicamos a vetorização.
# Observe que treinamos e aplicamos em treino e apenas aplicamos em teste
X_treino_vectors = vectorizer.fit_transform(X_treino)
X_teste_vectors = vectorizer.transform(X_teste)

# Criando 3 modelos com 3 algoritmoos diferentes

# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
modelo1 = LogisticRegression(multi_class = 'multinomial', solver = 'lbfgs', random_state = 30, max_iter = 1000)

# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
modelo2 = RandomForestClassifier(n_estimators = 1000, max_depth = 100, random_state = 1)

# https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
modelo3 = MultinomialNB()

# Lista para o resultado
resultado = []

# Iniciando o modelo de votação
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html
# https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier
voting_model = VotingClassifier(estimators = [ ('lg', modelo1), ('rf', modelo2), ('nb', modelo3) ], voting = 'soft')
print("\nModelo de Votação:\n")
print(voting_model)
    
# Treinamento
voting_model = voting_model.fit(X_treino_vectors, y_treino)
    
# Previsões com dados de teste
previsoes =  voting_model.predict(X_teste_vectors)

# Grava o resultado
resultado.append(accuracy_score(y_teste, previsoes))
    
# Print
print('\nAcurácia do Modelo:', accuracy_score(y_teste, previsoes),'\n')
print('\n')

