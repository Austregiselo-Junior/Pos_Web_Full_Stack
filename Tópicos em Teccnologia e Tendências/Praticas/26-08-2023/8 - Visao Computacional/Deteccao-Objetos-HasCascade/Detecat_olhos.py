# Import da bibliotea do OpenCV
import cv2

# Chamando e abrindo a WEBCAM
camera = cv2.VideoCapture(0)

# criando um classificador para detecção de objetos
classificador = cv2.CascadeClassifier(r'cascades/haarcascade_eye.xml')

# Desenvolvimento do projeto
while True:
    check,img = camera.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGray)

    # criando retangulo dos olhos das pessoas
    for x,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2)

    cv2.imshow('Imagem', img)
    cv2.waitKey(15)



