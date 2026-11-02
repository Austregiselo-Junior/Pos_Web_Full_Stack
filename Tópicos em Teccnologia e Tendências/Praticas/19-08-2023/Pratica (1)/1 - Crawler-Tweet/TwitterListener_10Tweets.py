# Conjunto de importações da biblioteca Tweepy
# Coletando os dados com os campos específicos do Twiiter.
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener_10Tweets(StreamListener):  
    #método de inicialização   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor máximo de tweets a serem coletados
        self.max_tweets = 1000 
        
    def on_data(self, data):
        #incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:
            #carrega e codifica os dados para o formato JSON
            tweet = json.loads(data)
            #Escreve o campo de data de publicação do tweet
            print("Data da publicacao do tweet")            
            print(tweet.get('created_at'))
            #Escreve o campo referente ao conteúdo do tweet
            print("Conteudo do tweet")
            print(tweet.get('text'))
            #Escreve o campo referente ao idioma do tweet
            print("Idioma do tweet")
            print(tweet.get('lang'))
            #Escreve o campo referente ao total de likes que o tweet recebeu
            print("Total de likes do tweet")
            print(tweet.get('favorite_count'))
        except BaseException as erro:
            print('Erro: ' + erro)
        #condição de parada
        if self.cont_tweet >= self.max_tweets:
            #retorne false
            return False

def coletar_tweets():
    #Complete aqui com o valor da "access_token" gerada para você - Novas chaves em: 01/05/2022 - Ricardo Roberto de Lima
    access_token = "742142292820152324-6sD5oCjn0jKiMiBZ43ldNWsdpBP0piD"
    #Complete aqui com o valor da "access_token_secret" gerada para você
    access_token_secret = "jGomaTTDJHotVqfRB407YAoXfwSrkSA6XyV1bG5VFMBbJ"
    #Complete aqui com o valor da "consumer_key" gerada para você
    consumer_key = "jee7tQ2U61gvF1Pg51HtEr2XE"
    #Complete aqui com o valor da "consumer_secret" gerada para você
    consumer_secret = "0tn6JUJ6uA5jFlPljrrLcnZDxW1M4uD1RK6SwZj1VDqhaZKPfY"

    tl = TwitterListener_10Tweets()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['Silvio Santos', 'Bolsonaro', 'Fantástico', 'Anita', 'Flamengo', 'Palmeiras'])

#chamada da função coletar_tweets()
coletar_tweets()


      #  consumerKey = 'jee7tQ2U61gvF1Pg51HtEr2XE'
      #  consumerSecret = '0tn6JUJ6uA5jFlPljrrLcnZDxW1M4uD1RK6SwZj1VDqhaZKPfY'
      #  accessToken = '742142292820152324-6sD5oCjn0jKiMiBZ43ldNWsdpBP0piD'
      #  accessTokenSecret = 'jGomaTTDJHotVqfRB407YAoXfwSrkSA6XyV1bG5VFMBbJ'