import cv2
import math
import numpy as np
#import Cascade_Haar as C
from matplotlib import pyplot as plt
def open_picture(img):
    #img = cv2.imread(img)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #D:\Git_project\VKR\CARS_ANOTHER    #D:\Git_project\VKR\CARS_ANOTHEROUPUT_ANOTHER

path = r"D:\Git_project\VKR\OUPUT_ANOTHER\0.png"
img = cv2.imread(path)
img2 = cv2.imread("gray1.png",)
blur = cv2.GaussianBlur(img2, (5, 5), 0)

#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,3)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.blur(img,(5,5))
ret,th = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#th3 = cv2.adaptiveThreshold(th,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#           cv2.THRESH_BINARY,11,17)
open_picture(th)
edges = cv2.Canny(th,50,100,apertureSize = 3)
open_picture(edges)
#lines = cv2.HoughLines(edges,1,np.pi/180,10,5,10)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, minLineLength=10, maxLineGap=100)
lines2 = cv2.HoughLinesP(edges, 1, np.pi / 2, threshold=500, minLineLength=500, maxLineGap=1)
print(lines)
angles = []
rows,cols,ch = img.shape
print(rows,cols,ch)
for i in range(0,len(lines)):
    for x, y, h,w in lines[i]:
        #cv2.line(img, (x, y), (h, w), (255, 255, 255), 1)
        print(x, y, h, w)
        tg = (w - y) / (h - x)

        if i == 2:
            cv2.line(img, (x, y), (h, w), (255, 255, 255), 2)
            cv2.line(img, (h, w), (h,y1), (255, 255, 255), 2)
            cv2.line(img, (x1, y1), (x1, y), (255, 255, 255), 2)
            cv2.rectangle(img, (x1, y), (h, y1), (255, 0, 0), 2)
            roi_color = img[y:y1, x1:h]

            #open_picture(img)
            tg1 = math.degrees(math.atan(tg))
            open_picture(img)
            open_picture(roi_color)


        if i == 0:
            x1 = x
            y1 = y
            h1 = h
            w1 = w
            cv2.line(img, (x, y), (h, w), (255, 255, 255), 2)
            #cv2.line(img, (x, y), (x,0), (255, 255, 255), 2)
            #open_picture(img)
            tg1 = math.degrees(math.atan(tg))

   # cv2.line(img, (x, y), (h, w), (255, 255, 255), 2)
  #  open_picture(img)

    res = math.degrees(math.atan(tg))
    angles.append(res)
rows,cols,ch = img.shape
print (angles)
a = [i for i in angles if i != 0.0]
print(len(a))
print(len(angles))
av = sum(angles)/len(a)
print(av,tg1)
M = cv2.getRotationMatrix2D((cols/2,rows/2),tg1,1)
dst = cv2.warpAffine(img,M,(cols,rows))
#C.save_picture(C.path_res,dst,0)


open_picture(dst)

