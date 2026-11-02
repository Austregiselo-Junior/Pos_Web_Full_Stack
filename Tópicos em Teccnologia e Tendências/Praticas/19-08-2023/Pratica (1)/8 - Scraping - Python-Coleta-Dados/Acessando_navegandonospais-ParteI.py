from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')
'''
print(soup.parent)

tag_title = soup.title

print(tag_title)
print(tag_title.parent)
print(soup.td.parent)
print(soup.td.parent.parent)
'''

for pai in soup.p.parents:
	print(pai.name)