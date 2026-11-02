import requests
from bs4 import BeautifulSoup

def get_http(url, nome_livro):

	nome_livro = nome_livro.replace(' ', '%20')
	url = '{0}?q={1}'.format(url, nome_livro)

	try:
		return requests.get(url)
	except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
				requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
		print(str(e))
	except Exception as e:
		raise

def get_produtos(content):

	soup = BeautifulSoup(content, 'lxml')
	produtos = soup.find_all('div', {'class':'cs-list-container'})

	lista_produtos = []
	for produto in produtos:
		info_produto = [produto.a.get('href'), produto.a.string]
		lista_produtos.append(info_produto)
	return lista_produtos

def get_http_page_produto(lista_produtos):

	d = {}
	lista_prod = []

	for produto in lista_produtos:

		try:
			r = requests.get(produto[0])
		except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
				requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
			print(str(e))
			r = None
		except Exception as e:
			raise

		d = parse_page_produto(r.text, produto[0], produto[1])
		lista_prod.append(d.copy())

	return lista_prod

		

def parse_page_produto(content, url_produto, titulo):

	soup = BeautifulSoup(content, 'lxml')
	
	div = soup.find('div', {'class':'container-product-image'})
	url_capa = div.a.img.get('src')
	preco = soup.find('span', {'class':'final-price no-extras'})

	d = {}
	try:
		preco = preco.string
		d = {
			'titulo':titulo,
			'Preco':preco,
			'url_capa':url_capa,
			'url_produto':url_produto
		}
	except AttributeError as e:
		pass

	return d


if __name__ == '__main__':

	url = 'http://busca.saraiva.com.br/'
	nome_livro = 'redes de computadores'

	r = get_http(url, nome_livro)

	if r:
		lista_produtos = get_produtos(r.text)
		lista = get_http_page_produto(lista_produtos)
		print(lista)