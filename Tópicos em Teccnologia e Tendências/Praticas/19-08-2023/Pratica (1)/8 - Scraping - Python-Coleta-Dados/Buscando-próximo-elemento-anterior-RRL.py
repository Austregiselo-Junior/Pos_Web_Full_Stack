from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

'''
producers = soup.find(id='producers')
tag_next = producers.find_next()
print(tag_next)

producers = soup.find(id='producers')
tag_next = producers.find_all_next()
print(tag_next)

producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_previous()
print(tag_previous)
'''

producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_all_previous()
print(tag_previous)