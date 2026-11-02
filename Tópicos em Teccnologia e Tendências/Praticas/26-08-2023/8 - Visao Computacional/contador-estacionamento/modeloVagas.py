#import das bibliotecas cv2 (opencv) e (pickle)

import cv2
import pickle

img = cv2.imread('estacionamento.png')

vagas = []

# Serve para salver todas as vagas em um só objeto para gravar.
for x in range(69):
    vaga = cv2.selectROI('vagas',img,False)
    cv2.destroyWindow('vagas')
    vagas.append(vaga)

# Este for serve pra selecionar cada uma das vagas com um rectangulo.
    for x,y,w,h in vagas:
        cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,0),2)

# Este bloco serve pra savar o arquivo fisicamente com a extensão pkl (vagastotal.pkl)
with open('vagastotal.pkl','wb') as arquivo:
    pickle.dump(vagas,arquivo)
