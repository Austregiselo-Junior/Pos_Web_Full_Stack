// Algoritmo para (Deteção de Faces)
// Data: 03 de Maio de 2018 - 14:14hs.
// Autor: Ricardo Roberto de Lima - Arquivo: Captura2 - Classificador.

import cv2

classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMuitiScale(imagemCinza, scaleFactor=1.5, minSize=(100,100))

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
    
    cv2.imshow("Face", imagem)
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
