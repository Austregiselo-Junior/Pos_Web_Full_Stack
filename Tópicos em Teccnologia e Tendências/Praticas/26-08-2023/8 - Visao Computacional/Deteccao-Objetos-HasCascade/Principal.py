import cv2

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_eye.xml')


while True:
    check,img = camera.read()

    imgGray = cv2.cvtColor(img,cv2.COLOR_BRG2GRAY)
    objetos = classificador.detectMultiScale(imgGray)

    # criando a Estrutura de Repetição para percorrer o objeto.

    for x, y, l, a in objetos:
        cv2.rectangle(img, (x,y), (x+y,y+a), (255,0,0),2)

    cv2.imshow('Imagem', img)
    cv2.waitKey(1)