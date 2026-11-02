// Algoritmo para (Deteção de Faces)
// Data: 03 de Maio de 2018 - 14:14hs.
// Autor: Ricardo Roberto de Lima - Arquivo: Captura.

import cv2

camera = cv2.VideoCapture(0)

while (True):
    conectado, imagem = camera.read()

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
