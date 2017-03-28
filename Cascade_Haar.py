from urllib.request import urlopen
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
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
    plt.imsave('1.png',img1)
    plt.show()

path1 = './cars'
path = r'D:\Github_project\VKR\cars\101.png'
plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,150,200,3,5)
plate = plate_cascade.detectMultiScale(gray,1.3,5)
for (x, y, w, h) in plate:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 80, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    roi_edges = edges [y:y + h, x:x + w]
    cv2.imwrite('Car_lisence/'+os.path.split(path)[1],roi_edges)
def for_all_picture(path):
    list_dir = os.listdir(path)
    for i in list_dir:
        plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
        path1 = path+'/'+i
        img = cv2.imread(path1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img,100,200)
        plate = plate_cascade.detectMultiScale(gray,1.3,5)
        for (x, y, w, h) in plate:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 80, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            roi_edges = edges [y:y + h, x:x + w]
            cv2.imwrite('Car_lisence/'+os.path.split(path1)[1],roi_gray)

#Завтра попробовать ерудхолдинг и разобраться в кани детектид разобрать в функции малтисеил и попробовать разобраться
#  посчитать тесаракт билиотеку
# в определении
#c(path)
#open_picture(gray)

open_two(img,roi_gray)
#for_all_picture(path1)



