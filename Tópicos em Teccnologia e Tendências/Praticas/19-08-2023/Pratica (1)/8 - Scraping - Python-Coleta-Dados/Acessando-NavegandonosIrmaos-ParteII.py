from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

#print(soup.next_sibling)
#print(soup.td)
#print(soup.td.parent)
#print(soup.td.next_sibling)
#print(soup.td.next_sibling.next_sibling)

'''
for sibling in soup.p.next_siblings:
	print(repr(sibling))
'''

for sibling in soup.p.previous_siblings:
	print(repr(sibling))