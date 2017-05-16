import cv2
import math
import numpy as np
import os
import Detect_lines as dec
import Copy_delete as C

def picture_digit(path):
    im = cv2.imread(path)
    array = np.array(im)
    array_one = []
    for i in array:
        for j in i:
            array_one.append(sum(j)/len(j))
            print(j)
    print(len(array_one))
    print(lol)
if __name__ == '__main__':
    picture_digit(r'D:\Git_project\VKR\NEW_ROI\0\41.png')