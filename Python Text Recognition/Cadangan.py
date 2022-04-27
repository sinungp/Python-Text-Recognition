import urllib.request
import cv2
from PIL import Image
from pytesseract import pytesseract

url='http://192.168.0.110:8080/video'
camera=cv2.VideoCapture(url)

while True:
    _,Image=camera.read()
    cv2.imshow('Text Recognition',Image)
    if cv2.waitKey(1)&0xFF==ord('s'):
        cv2.imwrite('test1.jpg',Image)
        break

camera.release()
cv2.destroyAllWindows()

def tesseract():
    Imagepath='test1.jpg'
    pytesseract.tesseract_cmd
    text=pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])