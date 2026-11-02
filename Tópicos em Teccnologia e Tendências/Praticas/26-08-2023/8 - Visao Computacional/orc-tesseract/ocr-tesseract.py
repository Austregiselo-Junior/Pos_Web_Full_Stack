import cv2

import pytesseract as pt 

pt.pytesseract_md = "C:\\Program Files (x32)\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('imgteste.JPG')

boxes = pt.pytesseract.image_to_boxes(img, lang='por')
dados = pt.pytesseract.image_to_data(img, lang='por')

imH, imW,_ = img.shape

for x,linha in enumerate(dados.splitlines()):
    if x!=0:
        # print(linha)
        linha = linha.split()
        print(linha)
        if len(linha) == 12:
            x, y, w, h = int(linha[6]), int(linha[7]), int(linha[8]), int(linha[9])
            palavra = linha[11]
            cv2.rectangle(img, (x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(img, palavra, (x,y+10),cv2.FONT_HERSHEY_SIMPLEX,1.(0,0,255),2)

cv2.imshow('Imagem',img)
cv2.waitKey(0)



