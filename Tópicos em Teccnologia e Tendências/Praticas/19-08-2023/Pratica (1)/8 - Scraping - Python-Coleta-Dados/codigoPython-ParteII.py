
'''
arq = open('arquivo.txt', 'w')
arq.write('python eh legal\n')
arq.write('curso de bs4')
arq.close()
'''

'''
arq = open('arquivo.txt', 'r')
print(arq.read())
arq.close()
'''

with open('arquivo.txt', 'r') as f:
	print(f.read())