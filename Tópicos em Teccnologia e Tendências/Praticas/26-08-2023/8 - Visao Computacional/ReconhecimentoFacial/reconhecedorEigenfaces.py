import cv2
import os

detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
reconhecedorFace = cv2.face.EigenFaceRecognizer_create()
reconhecedorFace.read("classificadorEigen.yml")
largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)
dicNomes = {}
def getNome():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]

    nId = {}
    for caminhoImagem in caminhos:
        nome = os.path.split(caminhoImagem)[-1].split('.')[0]
        id = os.path.split(caminhoImagem)[-1].split('.')[1]
        nId [str(id)] = nome
        nId[str(-1)] = "Desconhecido"
    return nId


dicNomes = getNome()
while(True):
    conectado, imagem = camera.read()

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor= 1.5, minSize= (30,30))

    for(x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        cv2.rectangle(imagem,(x, y), (x + l, y + a), (0,0,255), 2 )
        id, confianca = reconhecedorFace.predict(imagemFace)
        print(id)
        cv2.putText(imagem,dicNomes[str(id)], (x,y + (a + 30)), font, 2,(0,0,255))
        cv2.putText(imagem, str(confianca), (x, y + (a + 50)), font, 1, (0, 0, 255))

    cv2.imshow('Face', imagem)
    if cv2.waitKey(1) == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()