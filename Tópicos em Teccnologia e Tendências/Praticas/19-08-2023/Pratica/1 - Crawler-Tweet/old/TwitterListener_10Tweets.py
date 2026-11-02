#Conjunto de importações da biblioteca Tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener_10Tweets(StreamListener):  
    #método de inicialização   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor máximo de tweets a serem coletados
        self.max_tweets = 10 
        
    def on_data(self, data):
        #incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:
            #escreve o conteúdo do tweet que chegou
            print (data)
        except BaseException as erro:
            print('Erro: ' + erro)
        #condição de parada: se o valor do contador de tweets é maior ou igual ao valor de condição de parada
        if self.cont_tweet >= self.max_tweets:
            #retorne false
            return False

def coletar_tweets():
    #Complete aqui com o valor da "access_token" gerada para você
    access_token = "742142292820152324-7iVz7ar3Pqhr9Tf64Yos9bUUcnvTy0x"
    #Complete aqui com o valor da "access_token_secret" gerada para você
    access_token_secret = "NsdSuxhODT3S276tGNS7OAe2rId3MBJiYgN73AeaXw7se"
    #Complete aqui com o valor da "consumer_key" gerada para você
    consumer_key = "H3kTS7SwZAA9ISrY8qqVNKeEQ"
    #Complete aqui com o valor da "consumer_secret" gerada para você
    consumer_secret = " cZ1gGOZjzx4vaOm9qUlX0BOfzi6RtElzjbW6AHcl6KMcOoi0uP"

    tl = TwitterListener_10Tweets()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['python', 'javascript', 'ruby'])

#chamada da função coletar_tweets()
coletar_tweets()
