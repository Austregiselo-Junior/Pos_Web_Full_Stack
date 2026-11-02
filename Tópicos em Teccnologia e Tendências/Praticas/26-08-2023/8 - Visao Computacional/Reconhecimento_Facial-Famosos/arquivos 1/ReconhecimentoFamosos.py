import cv2
import face_recognition as fr

imgElon = fr.load_image_file('arquivos/Elon.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

cv2.imshow('Elon', imgElon)
cv2.waitKey(0)

