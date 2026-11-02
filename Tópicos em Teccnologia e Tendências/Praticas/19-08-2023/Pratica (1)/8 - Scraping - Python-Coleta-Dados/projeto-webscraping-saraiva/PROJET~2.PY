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

def parse_html(content):
	soup = BeautifulSoup(content, 'lxml')

	produtos = soup.find_all('table')[10].find_all('td')

	"""f = open('td.html', 'w', encoding='utf-8')

	for produto in produtos:
		f.write(str(produto))
		f.write('\n\n\n')

	f.close()"""
	lista_produtos = []
	for produto in produtos:
		for string in produto.stripped_strings:
			if(string == 'Esgotado'):
				continue
			lista_produtos.append(string)
	print(lista_produtos)




if __name__ == '__main__':
	url = 'http://www.novatec.com.br/busca.php'
	#nome_livro = input("nome do livro: ")
	nome_livro = 'redes de computadores'
	r = post_http(url, nome_livro)
	
	if r:
		parse_html(r.text)
