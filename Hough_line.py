import cv2
import numpy as np
import math
from PIL import Image

path1 = "gray1.png"
# im = Image.open(path1)
# out = im.rotate(10)
# out.save("gray2.png","png")
img = cv2.imread(path1)
img =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,3)
edges = cv2.Canny(th3, 5, 10)
cv2.imshow('lol',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, minLineLength=20, maxLineGap=200)
#print(lines)
hough = np.zeros(img.shape, np.uint8)

print(tg)
res = math.degrees(math.atan(tg))
print(res)
#1.7899106082460694
path = './cars/2.png'
im = Image.open(path1)
out = im.rotate(res)
out.save("put.png","png")
out.show()

cv2.imshow('lol',roi_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


