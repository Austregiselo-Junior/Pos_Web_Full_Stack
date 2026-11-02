import cv2
import os
import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create() ##criando classificadores
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create(threshold= 60)

def getImagemComId():#função que tem como objetivo capturar o caminho e ler as imagens
    caminhos = [os.path.join('fotos',  f) for f in os.listdir('fotos')]#caminhos das imagens
    #print(caminhos)
    faces = []
    ids = []

    for caminhoImagem in caminhos:#pega o caminho das imagens
        imagemFace = cv2.imread(caminhoImagem, cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        #print(id)
        ids.append(id)
        faces.append(imagemFace)
    return np.array(ids) , faces #nparray é o formato necessario para fazer o treinamento

ids, faces = getImagemComId()
#print(faces)

#print(ids)
print('Treinando...')
#gera e treina os classificadores
eigenface.train(faces, ids)
eigenface.write('classificadorEigen.yml')
fisherface.train(faces,ids)
fisherface.write('classificadorFisher.yml')
lbph.train(faces,ids)
lbph.write('classificadorLBPH.yml')
print("treinamento concluido")