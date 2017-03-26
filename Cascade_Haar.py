from urllib.request import urlopen
import cv2
import math
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
plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plate = plate_cascade.detectMultiScale(gray, 1.3,5)
for (x, y, w, h) in plate:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 80, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    cv2.imwrite('gray.png',roi_gray)
#c(path)
#open_picture(path1)
#open_two(img,roi_gray)


img = cv2.imread(path1)
img =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,3)
edges = cv2.Canny(th3, 80, 120)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, minLineLength=50, maxLineGap=80)

hough = np.zeros(img.shape, np.uint8)


for x,y,h,w in lines[0]:
    cv2.line(img,(x,y),(h,w),(0,255,0),2)
    roi_gray = img[y:y + h-2, x:x + w-2]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
