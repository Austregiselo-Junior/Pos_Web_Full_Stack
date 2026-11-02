import requests
from bs4 import BeautifulSoup
import saraiva
import novatec

def func_novatec(nome_livro):
	url = 'http://www.novatec.com.br/busca.php'
	r = novatec.post_http(url, nome_livro)
	lista_produto = []
	if r:
		lista_produto = novatec.parse_html(r.text)
	return lista_produto

def func_saraiva(nome_livro):
	url = 'http://busca.saraiva.com.br/'	
	r = saraiva.get_http(url, nome_livro)
	if r:
		lista_produtos = saraiva.get_produtos(r.text)
		lista = saraiva.get_http_page_produto(lista_produtos)
	return lista

def main(nome_livro):
	d_produtos = {}
	lista_produto = func_novatec(nome_livro)
	d_produtos.update({'novatec':lista_produto})

	lista_produto = func_saraiva(nome_livro)
	d_produtos.update({'novatec':lista_produto})

	return d_produtos



if __name__ == '__main__':
	nome_livro = 'redes de computadores'
	d_produtos = main(nome_livro)
	print(d_produtos)
	
	
	
