#Primeira Aula Prática - Coleta de Dados com Python e BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = 'http://servicos2.sjc.sp.gov.br/mapa_google_itinerario.aspx'
re = requests.get(url)

soup = BeautifulSoup(re.text, 'lxml')

lista_itinerarios = soup.find_all('table', class_='textosm')
#print(lista_itinerarios)

url='http://servicos2.sjc.sp.gov.br'
for lista_td in lista_itinerarios:
    print(lista_td.find_all('td'))
    for lista_dados in lista:
        print(lista_dados.next_element)
    
