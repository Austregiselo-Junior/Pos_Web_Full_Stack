#Primeira Aula Prática - Coleta de Dados com Python e BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = 'http://servicos2.sjc.sp.gov.br/mapa_google_itinerario.aspx'
re = requests.get(url)

print(re.text)
