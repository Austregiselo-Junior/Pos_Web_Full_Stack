import requests
from bs4 import BeautifulSoup

def get_http(url, nome_livro):

	nome_livro = nome_livro.replace(' ', '%20')
	url = '{0}?q={1}'.format(url, nome_livro)

	try:
		return requests.get(url)
	except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
				requests.excepetions.ConnectionError, requests.exceptions.Timeout) as e:
		print(str(e))
		pass
	except Exception as e:
		raise

if __name__ == '__main__':

	url = 'http://busca.saraiva.com.br/'
	nome_livro = 'redes de computadores'

	r = get_http(url, nome_livro)

	with open('result.html', 'w') as f:
		f.write(r.text)