# Projeto 3 - Modelagem de Tópicos do Noticiário Financeiro

# Versão 3 - Stacking

# Imports
import numpy as np
from nltk.corpus import stopwords
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.metrics import accuracy_score

# Carregando os dados
noticias = load_files('dados', encoding = 'utf-8', decode_error = 'replace')

# Separando variáveis de entrada e saída
X = noticias.data
y = noticias.target

# Lista de stop words
my_stop_words = set(stopwords.words('english'))

# Divisão em treino e teste (70/30)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.30, random_state = 93)

# Vetorização
vectorizer = TfidfVectorizer(norm = None, stop_words = my_stop_words, max_features = 1000, decode_error = "ignore")

# Aplicamos a vetorização.
# Observe que treinamos e aplicamos em treino e apenas aplicamos em teste
X_treino_vectors = vectorizer.fit_transform(X_treino)
X_teste_vectors = vectorizer.transform(X_teste)

# Inicializando os modelos base
modelos_base = [('rf', RandomForestClassifier(n_estimators = 100, random_state = 42)), ('nb', MultinomialNB())]

# Stacking
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html
# https://scikit-learn.org/stable/modules/ensemble.html#stacking
stacking_model = StackingClassifier(estimators = modelos_base, final_estimator = LogisticRegression(multi_class = 'multinomial', random_state = 30, max_iter = 1000))
print("\nModelo de Votação:\n")
print(stacking_model)

# Treinamento
acuracia = stacking_model.fit(X_treino_vectors.todense(), y_treino).score(X_teste_vectors.todense(), y_teste)

# Lista para o resultado
resultado = []
resultado.append(acuracia)

# Print
print('\nAcurácia do Modelo:', acuracia, '\n')
print('\n')

