from urllib.request import urlopen
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
import os
import Copy_delete as cop
url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_russian_plate_number.xml'
path = './CARS_ANOTHER/0.png'
OUT = 'OUPUT_ANOTHER/'
path_res = "./CARS_ANOTHER/"
#FOR UNDETECTED_CARS # path=r'D:\Git_project\VKR\UNDETECTED_CARS\42.png'


# Cкачиваение тренировочного файла
def download(url):
    logo = urlopen(url).read()
    f = open("haarcascade_russian_plate_number.xml", "wb")
    f.write(logo)
    f.close()
#conver to gray threshold picture
def threthholding(path):
    img = cv2.imread(path)
    #img = cv2.GaussianBlur(img, (5, 5), 0)
    # th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,3)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.blur(img, (5, 5))
    gray = cv2.GaussianBlur(gray, (3, 3), 0);
    ret, th = cv2.threshold(gray, 140, 255, 0)
    return th
def Conver_all_picture(path,path_out):
    lst_fl = os.listdir(path)
    for i in lst_fl:
        a = threthholding(path+i)
        save_picture(path,a,i.split('.')[0])



# Показ одной картинки

def open_picture(img):
    # img = cv2.imread(img)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    #print(res)
    cv2.destroyAllWindows()

def move_file(path_in,path_out,path_out1,img):
    cv2.imshow('image', img)
    res = cv2.waitKey(0)
    lst = os.listdir(path_in)
    if res == 100:
        save_picture()
        cv2.destroyAllWindows()
    else:
        cv2.destroyAllWindows()

    # print(res)
    cv2.destroyAllWindows()


# Показ двух картинок
def open_two(img1, img2):
    plt.subplot(121)
    plt.imshow(img1, cmap='gray')
    plt.title('Original Image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(img2, cmap='gray')
    plt.title('Plate Image'), plt.xticks([]), plt.yticks([])
    plt.show()


def save_picture(OUT, img, i):
    cv2.imwrite(OUT + '{0}'.format(i), img)


# path = "put.png"
def Cascade(path):
    plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
    img = cv2.imread(path)
    # open_picture(gray)
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plaques = plate_cascade.detectMultiScale(gray, 1.3, 5)
        for i, (x, y, w, h) in enumerate(plaques):
            roi_color = img[y:y + h, x:x + w]
            r = 300.0 / roi_color.shape[1]
            dim = (300, int(roi_color.shape[0] * r))
            resized = cv2.resize(roi_color, dim, interpolation=cv2.INTER_AREA)
        return resized
    except:
        flag = False
        print("Error")
        #os.remove(path)


def all_cascade(path, OUT):
    path_tmp = path
    lst = os.listdir(path)
    print(lst)
    c = 1
    for i in lst:
        path += i
        a = Cascade(path)
        print(a)

        save_picture(OUT, a, i)
        path = path_tmp
        c += 1
if __name__ == '__main__':

        #a = Cascade(path)
       # for i in os.listdir(OUT):
        #    a = threthholding(path=r"D:\Git_project\VKR\OUPUT_ANOTHER\{0}".format(i))
        #    open_picture(a)
        all_cascade(path_res, OUT)
        # a = Cascade(path)
        # open_picture(roi_color)

        # c(path)
        # open_picture(path1)
        # open_two(img,roi_gray)



        # save_canny(path1)
