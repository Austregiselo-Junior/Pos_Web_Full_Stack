#Primeira Aula Prática - Coleta de Dados com Python e BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = 'http://servicos2.sjc.sp.gov.br/mapa_google_itinerario.aspx'
re = requests.get(url)

soup = BeautifulSoup(re.text, 'lxml')

lista_itinerarios = soup.find_all('table', class_='textosm')
#print(lista_itinerarios)

#URL do Site com informações gerais da Raiz do Site
url='http://servicos2.sjc.sp.gov.br'

#Laço para iteirar os elementos HTML em forma de listas.
for lista_td in lista_itinerarios:
    print(lista_td.find_all('td'))
    for lista_dados in lista:
        print(lista_dados.next_element)
        if lista_dados.next_element.name == 'a':
            url_it = '{0}{1}'.format(url,lista_dados.next_element.get('href'))
            print(url_it)
        else:
            print(lista_dados.next_element)
            

    
