from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

'''
tag_list = soup.find_all('ul')
print(tag_list)

tag_list = soup.find_all(['ul', 'div'])
print(tag_list)

tag_list = soup.find_all('ul', limit=2)
print(tag_list)

tag_list = soup.find_all(string='rabbit')
print(tag_list)

tag_list = soup.find_all(string=True)
print(tag_list)

tag_list = soup.find_all(string=['rabbit', 'bear'])
print(tag_list)

tag_list = soup.find_all(class_=['producerlist', 'primaryconsumerlist'])
print(tag_list)

tag_list = soup.ul.find_all('div')
print(tag_list)
'''

tag_list = soup.find_all('div', class_='name')
print(tag_list)