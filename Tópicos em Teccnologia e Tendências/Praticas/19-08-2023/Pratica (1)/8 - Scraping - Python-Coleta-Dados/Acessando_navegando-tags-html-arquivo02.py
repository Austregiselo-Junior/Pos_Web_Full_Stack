from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

print(soup.title)
print(soup.head.title)
print(soup.a)
print(soup.a.img)
print(soup.td)
print(soup.tr)
print(soup.tr.td)
print(soup.td.attrs)
print(soup.td['class'])
print(soup.td['class'][0])
