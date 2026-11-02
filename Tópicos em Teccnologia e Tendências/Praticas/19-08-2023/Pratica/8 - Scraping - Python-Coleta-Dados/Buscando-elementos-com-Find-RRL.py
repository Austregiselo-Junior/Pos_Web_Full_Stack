from bs4 import BeautifulSoup

with open('arquivo04.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

'''
tag = soup.find('li')
print(tag)

tag = soup.find(string='plants')
print(tag)

tag = soup.find(string='bear')
print(tag)

tag = soup.find(id='primaryconsumers')
print(tag)

tag = soup.find(attrs={'class':'primaryconsumerlist'})
print(tag)

tag = soup.find(class_='primaryconsumerlist')
print(tag)

tag = soup.find('li', attrs={'class':'producerlist'})
print(tag)

tag = soup.ul.li.find('li')
print(tag)
'''

def is_sencondary_consumers(tag):
	return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

secondary_consumer = soup.find(is_sencondary_consumers)
print(secondary_consumer.li.div.string)