from bs4 import BeautifulSoup

with open('arquivo04.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')


primaryconsumers = soup.find_all(class_='primaryconsumerlist')
primaryconsumer = primaryconsumers[0]
#print(primaryconsumer)

'''
parent_ul = primaryconsumer.find_parents('ul')
print(parent_ul)
'''

parent_ul = primaryconsumer.find_parent('ul')
print(parent_ul)