# import das bibliotecas do opencv
import cv2

# chamando para abrir o vídeo Mp4.
camera = cv2.VideoCapture('video.mp4')

classificador = cv2.CascadeClassifier(r'cascades/haarcascade_fullbody.xml')

while True:
    check,img = camera.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGray,minSize=(50,50),scaleFactor=1.5)

    # realizar a detecção dos objetos com retangulo.
    for x,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l,y+a),(255,255,0),2)

    cv2.imshow('Imagem', img)
    cv2.waitKey(20)

