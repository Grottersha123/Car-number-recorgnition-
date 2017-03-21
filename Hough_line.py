import cv2
import numpy as np
path1 = ""
img = cv2.imread(path1)
img =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,111,3)
edges = cv2.Canny(th3, 80, 120)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 20, minLineLength=50, maxLineGap=80)

hough = np.zeros(img.shape, np.uint8)


for x,y,h,w in lines[0]:
    cv2.line(img,(x,y),(h,w),(0,255,0),2)
    roi_gray = img[y:y + h-2, x:x + w-2]