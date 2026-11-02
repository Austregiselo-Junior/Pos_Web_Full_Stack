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
	url = 'http://www.novatec.com.br/'
	url_capa = ''
	url_produto = ''
	for produto in produtos:
		tag_a = produto.find('a')
		if tag_a:
			if tag_a.next_element.next_element.name == 'img':
				url_capa = "{0}{1}".format(url, tag_a.img.get('src'))
				url_produto = "{0}{1}".format(url, tag_a.get('href'))
				lista_produtos.append(url_capa)				
				lista_produtos.append(url_produto)

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
