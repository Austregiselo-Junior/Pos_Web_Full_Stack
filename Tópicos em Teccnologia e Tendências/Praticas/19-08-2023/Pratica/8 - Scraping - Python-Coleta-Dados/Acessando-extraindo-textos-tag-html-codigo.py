from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
	soup = BeautifulSoup(f, 'html5lib')

#print(soup.prettify())
#print(soup.get_text())
#print(soup.p.get_text())
#print(soup.p.string)

print(soup.p.b.string)