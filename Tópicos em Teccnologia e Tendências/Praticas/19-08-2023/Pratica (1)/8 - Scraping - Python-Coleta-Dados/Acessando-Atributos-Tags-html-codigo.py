from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
	soup = BeautifulSoup(f, 'html.parser')

print(soup.p['class'])
print(soup.p.attrs)
print(soup.a['href'])
print(soup.a.get('href'))