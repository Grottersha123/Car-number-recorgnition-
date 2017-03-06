import cv2
import numpy as np
from matplotlib import pyplot as plt
cars = ['1','2','3','4','5']
"""for i in cars:
    img = cv2.imread('D:/Python/Diplom/cars/'+i+'.png',0)
    edges = cv2.Canny(img,500,400,3,3)

    #plt.imshow(img,cmap = 'gray')
   # plt.title('Original Image')
    #plt.xticks([])
    #plt.yticks([])
   # plt.subplot(122),
    plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    """
"""edges = cv2.
"""
img = cv2.imread('D:/Python/Diplom/cars/1.png',0)
gray = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
ed = cv2.Canny(gray,100,200)
plt.title('Original Image')
plt.subplot(121)
plt.imshow(gray,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.subplot(122),
plt.imshow(ed,cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()



