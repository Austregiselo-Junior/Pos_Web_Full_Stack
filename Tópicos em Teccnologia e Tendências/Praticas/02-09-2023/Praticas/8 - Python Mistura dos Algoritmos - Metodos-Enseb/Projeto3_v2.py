# Projeto 3 - Modelagem de Tópicos do Noticiário Financeiro

# Versão 2 - Otimização de Hiperpparâmetros para o Voting

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

# Para gravar o resultado
d = {}
d['soft'] = []
d['hard'] = []

# Loop
for x in range(1,100):

	# Divisão treino/teste
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.30, random_state = x)

    # Stop words
    my_stop_words = set(stopwords.words('english'))

    # Vetorização
    vectorizer = TfidfVectorizer(norm = None, stop_words = my_stop_words, max_features = 1000, decode_error = "ignore")

    # Aplica a vetorização
    X_treino_vectors = vectorizer.fit_transform(X_treino)
    X_teste_vectors = vectorizer.transform(X_teste)

    # Cria os modelos base
    modelo1 = LogisticRegression(multi_class = 'multinomial', solver = 'lbfgs', random_state = 30, max_iter = 1000)
    modelo2 = RandomForestClassifier(n_estimators = 1000, max_depth = 100, random_state = 1)
    modelo3 = MultinomialNB()

    # Loop
    for i in ['soft','hard']:
        voting_model = VotingClassifier(estimators = [ ('lg', modelo1), ('rf', modelo2), ('nb', modelo3)], voting = i)
        voting_model = voting_model.fit(X_treino_vectors, y_treino)
        previsoes = voting_model.predict(X_teste_vectors)
        print('-Random State:', x, '-Voting:', i, '-Acurácia :', accuracy_score(y_teste, previsoes))
        d[i].append((x,accuracy_score(y_teste, previsoes)))
    

print('\nMelhores Resultados:')

# Extrai os melhores resultados
h = max(d['hard'], key = lambda x:x[1])
s = max(d['soft'], key = lambda x:x[1])

# Print
print('-Random State:',h[0], '-Voting:hard', '-Acurácia:', h[1])
print('-Random State:',s[0], '-Voting:soft', '-Acurácia:', s[1])

print('\n')



