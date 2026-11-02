import requests
from bs4 import BeautifulSoup

#novatec

def post_http(url, nome_livro):
	payload = {'palavra':nome_livro,
			'enviar':'Buscar'}

	try:
		return requests.post(url, data=payload)
	except (requests.exceptions.HTTPError, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
		print(str(e))
		pass
	except Exception as e:
		raise
	return None


if __name__ == '__main__':
	url = 'http://www.novatec.com.br/busca.php'
	#nome_livro = input("nome do livro: ")
	nome_livro = 'redes de computadores'
	r = post_http(url, nome_livro)
	with open('result.html', 'w', encoding='utf-8') as f:
		f.write(r.text)
