from urllib.request import urlopen
import cv2
import numpy as np
from matplotlib import pyplot as plt
url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_russian_plate_number.xml'


#Cкачиваение тренировочного файла
def download(url):
    logo = urlopen(url).read()
    f = open("haarcascade_russian_plate_number.xml", "wb")
    f.write(logo)
    f.close()
# Показ одной картинки

def open_picture(img):
    img = cv2.imread(img)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Показ двух картинок
def open_two(img1,img2):
    plt.subplot(121)
    plt.imshow(img1,cmap='gray')
    plt.title('Original Image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(img2,cmap='gray')
    plt.title('Plate Image'), plt.xticks([]), plt.yticks([])
    plt.show()

path = './cars/1.png'
path1 = 'gray.png'
def c(path):
    plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plate = plate_cascade.detectMultiScale(gray, 1.3,5)
    for (x, y, w, h) in plate:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 80, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
    cv2.imwrite('gray.png',roi_color)
c(path)
open_picture(path1)
#open_two(img,roi_color)



