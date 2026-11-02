from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
	soup = BeautifulSoup(f, 'lxml')

'''
producers = soup.find(id='producers')
next_sibling = producers.find_next_sibling()
print(next_sibling)
'''

'''
producers = soup.find(id='producers')
next_siblings = producers.find_next_siblings()
print(next_siblings)
'''

'''
producers = soup.find(id='quaternaryconsumers')
previous_sibling = producers.find_previous_sibling()
print(previous_sibling)
'''

producers = soup.find(id='quaternaryconsumers')
previous_siblings = producers.find_previous_siblings()
print(previous_siblings)