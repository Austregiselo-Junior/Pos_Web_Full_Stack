from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

tag = soup.title
print(tag)

print(tag.name)

tag = soup.p
print(tag.name)
