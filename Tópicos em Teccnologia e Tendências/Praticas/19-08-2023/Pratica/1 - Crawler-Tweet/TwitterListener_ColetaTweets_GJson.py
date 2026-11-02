# Conjunto de importações
# Implementação do Código para Captura dos Dados no Twitter e gravação em arquivo do tipo Json..
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener(StreamListener):  
    #método de inicialização   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor máximo de tweets a ser coletado
        self.max_tweets = 100 
        
    def on_data(self, data):
        #incrementa o contador de tweets 
        self.cont_tweet = self.cont_tweet + 1
        try:
            print(data)
            #converte o tweet para o formato json
            tweet = json.loads(data) 
            #cria e carrega o arquivo 'twitter_data.json'
            #o argumento mode='a' indica que será realizada a operação append
            with open('twitter_data.json', mode='a') as meu_arquivo:
                #salva o tweet no arquivo com identação
                json.dump(tweet, meu_arquivo, indent=4) 
        except BaseException as erro:
            print('Erro: ' + erro)
        #condição de parada
        if self.cont_tweet >= self.max_tweets:
             #retorne false
             return False

def coletar_tweets():
    #Complete aqui com o valor da "access_token" gerada para você - Novas chaves em: 01/05/2022 - Ricardo Roberto de Lima
    access_token = "742142292820152324-sxXgUn9OeTuGSTVLkZrhpiZbkB9ekhk"
    #Complete aqui com o valor da "access_token_secret" gerada para você
    access_token_secret = "KsbuXCygHapZwyr9bCBwpNGRIvEz9G5z4yEBdMR6vylBT"
    #Complete aqui com o valor da "consumer_key" gerada para você
    consumer_key = "1Yoau6FaXoRT7hfmMCZFOyMMY"
    #Complete aqui com o valor da "consumer_secret" gerada para você
    consumer_secret = "Qt0g2IFQ2fpCyPaHzNc9EOKJYfu2hPDFielrr7wdB7qrAVXlVJ"

    tl = TwitterListener()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['Neymar', 'Brasil', 'Copa'])

#chamada da função coletar_tweets()
coletar_tweets()
