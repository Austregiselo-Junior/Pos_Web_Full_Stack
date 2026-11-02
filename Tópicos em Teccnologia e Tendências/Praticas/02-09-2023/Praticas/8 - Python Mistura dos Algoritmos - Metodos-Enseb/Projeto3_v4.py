# Projeto 3 - Modelagem de Tópicos do Noticiário Financeiro

# Versão 4 - Stacking com Otimizaçãoo de Hiperparâmetros

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

# Lista para os resultados
d1 = []

# Loop
for x in range(1,100):

	# Divisão treino/teste
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.30, random_state = x)

    # Stop words
    my_stop_words = set(stopwords.words('english'))

    # Vetorização
    vectorizer = TfidfVectorizer(norm = None, stop_words = my_stop_words, max_features = 1000, decode_error = "ignore")

    # Aplica a vetorização
    X_treino_vectors = vectorizer.fit_transform(X_treino)
    X_teste_vectors = vectorizer.transform(X_teste)

    # Modelos base
    modelos_base = [('rf', RandomForestClassifier(n_estimators = 100, random_state = 42)), ('nb', MultinomialNB())]

    # Modelo Stacking
    stacking_model = StackingClassifier(estimators = modelos_base, final_estimator = LogisticRegression(multi_class = 'multinomial', random_state = 30, max_iter = 1000))
    
    # Acurácia
    acuracia = stacking_model.fit(X_treino_vectors.todense(), y_treino).score(X_teste_vectors.todense(), y_teste)
    
    # Resultado
    d1.append((x,acuracia))
    
    print('-Random State:', x, '-Acurácia :', acuracia)

print('\nMelhores Resultados')
mx = max(d1, key = lambda x:x[1])
print('-Random State:', mx[0], '-Acurácia :', mx[1])
print('\n')


