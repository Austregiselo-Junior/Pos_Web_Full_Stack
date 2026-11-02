import cv2
import numpy as np

classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")##carrega o xml classificador que contem o treinamento para a detecção de faces
classificadorOlho = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")## carrega o xml classificador para detecç~çao de olhos
camera = cv2.VideoCapture(0)##seleciona a camera que será usada
amostra = 1 ##controla quantas fotos foram tiradas
numeroAmostras = 25 ## tirar 25 fotos de cada pessoa para o aprendizado
largura, altura = 220, 220 ## controla o tamanho da imagem que será tirada


print("Capturando as faces...")

nome = input("Digite seu nome: ")
id = input("Digite seu id: ")


while(True):##Captura da imagem
    conectado, imagem = camera.read()##lê a camera que foi selecionada e ja dentro das variaveis
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)##transforma a imagem colorida em tons de cinza, o programa trabalha melhor assim
    facesDetectadas = classificador.detectMultiScale(imagemCinza,scaleFactor=1.5,minSize=(150,150))

    #print(np.average(imagemCinza))

    if amostra >= numeroAmostras + 1:
        break

    for (x, y, l, a) in facesDetectadas:#coloca o retando na faca
        cv2.rectangle(imagem, (x,y), (x + l, y + a),(0, 0, 255), 2 )##Tamanho do retangulo
        regiao = imagem[y:y + a, x:x + l] # capturando apenas um pedaço da imagem
        regiaoCinzaOlho = cv2.cvtColor(regiao,cv2.COLOR_BGR2GRAY)#transforma a regiao em escala de cinza
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        for(ox ,oy, oAltura, oLargura) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + oLargura, oy + oAltura), (0, 255, 0), 2)

            if cv2.waitKey(1) & 0xFF == ord('q'):## toda vez que a tecla q for apertada ele vai executar o codigo do if, usaremos isso para capturar a imagem
                if np.average(imagemCinza) > 110:## aqui ele vai verificar se a imagem esta muito escura para ser capturada
                    imagemFace = cv2.resize(imagemCinza[y:y + a, x:x  + l], (largura,altura))## imagem cinza redimensionada
                    cv2.imwrite("fotos/" +nome+ "." + str(id) + '.' + str(amostra) + '.jpg', imagemFace)#formato de salvar a imagem Nome.(nº da foto)
                    print('Foto nº '+ str(amostra)+'Tirada com sucesso!')
                    amostra += 1


    cv2.imshow("Face", imagem)
    cv2.waitKey(1)

print('Faces capturadas com sucesso')

camera.release()
cv2.destroyAllWindows()