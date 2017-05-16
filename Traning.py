import cv2
import numpy as np
import Segmentation as s

import Detect_lines as d
# ============================================================================

def reduce_colors(img, n):
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = n
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    return res2

# ============================================================================

def clean_image(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(gray_img
        , None
        , fx=5.0
        , fy=5.0
        , interpolation=cv2.INTER_CUBIC)


    resized_img = cv2.GaussianBlur(resized_img,(5,5),0)
    cv2.imwrite('licence_plate_large.png', resized_img)

    equalized_img = cv2.equalizeHist(resized_img)
    cv2.imwrite('licence_plate_equ.png', equalized_img)


    reduced = cv2.cvtColor(reduce_colors(cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR), 8), cv2.COLOR_BGR2GRAY)
    cv2.imwrite('licence_plate_red.png', reduced)


    ret, mask = cv2.threshold(reduced, 64, 255, cv2.THRESH_BINARY)
    cv2.imwrite('licence_plate_mask.png', mask)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    mask = cv2.erode(mask, kernel, iterations = 1)
    cv2.imwrite('licence_plate_mask2.png', mask)

    return mask

# ============================================================================

def find_license(path):
    im = cv2.imread(path)
    height, width = im.shape[:2]
    h_coef_min = 14
    h_coef_max = 80

    w_coef_min = 10
    w_coef_max = 30

    h_max = height * h_coef_max / 100
    h_min = height * h_coef_min / 100

    w_max = width * w_coef_max / 100
    w_min = width * w_coef_min / 100
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:20]
    a = []
    for c in contours:
        peri = cv2.arcLength(c, True)
        ap = cv2.approxPolyDP(c, 0.02 * peri, True)
        oh = s.max_min(ap)
        point1, point2 = s.max_min(ap)
        t = s.take_character((h_min, h_max), (w_min, w_max), point1, point2)
        if t:
            # print(len(ap))
            a.append(oh)
            # cv2.rectangle(im, point1, point2, (255, 22, 0), 2)
            # print(a)
            # dec.open_picture(im)

    a.sort()

    ter = s.delete_crosses(a)
    for point1, point2 in ter:
        cv2.rectangle(im, point1, point2, (255, 22, 0), 2)
    return im

def extract_characters(img):
    bw_image = cv2.bitwise_xor(img)
    contours = cv2.findContours(bw_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]
    height, width = img.shape[:2]
    h_coef_min = 14
    h_coef_max = 80

    w_coef_min = 10
    w_coef_max = 30

    h_max = height * h_coef_max / 100
    h_min = height * h_coef_min / 100

    w_max = width * w_coef_max / 100
    w_min = width * w_coef_min / 100
    char_mask = np.zeros_like(img)
    bounding_boxes = []
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:20]
    for c in contours:
        #x,y,w,h = cv2.boundingRect(contour)
        ## bounding_boxes.append((center, (x,y,w,h)))
        peri = cv2.arcLength(c, True)
        ap = cv2.approxPolyDP(c, 0.02 * peri, True)
        oh = s.max_min(ap)
        point1, point2 = s.max_min(ap)
        t = s.take_character((h_min, h_max), (w_min, w_max), point1, point2)
        a = []
        if t:
            # print(len(ap))
            a.append(oh)
            cv2.rectangle(char_mask, point1,point2, 255, -1)
            # cv2.rectangle(im, point1, point2, (255, 22, 0), 2)
            # print(a)
            # dec.open_picture(im)
    a.sort()

    ter = s.delete_crosses(a)
    for point1, point2 in ter:
        cv2.rectangle(char_mask, point1, point2, 255,-1)
        #cv2.rectangle(char_mask,(x,y),(x+w,y+h),255,-1)


    cv2.imwrite(r'licence_plate_mask3.png', char_mask)

    clean = cv2.bitwise_not(cv2.bitwise_and(char_mask, char_mask, mask = bw_image))

    #bounding_boxes = sorted(bounding_boxes, key=lambda item: item[0][0])

    characters = []
    for center, bbox in bounding_boxes:
        x,y,w,h = bbox
        char_image = clean[y:y+h,x:x+w]
        characters.append((bbox, char_image))

    return clean, characters


def highlight_characters(img, chars):
    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for bbox, char_img in chars:
        x,y,w,h = bbox
        cv2.rectangle(output_img,(x,y),(x+w,y+h),255,1)

    return output_img

# ============================================================================

img = cv2.imread(r'D:\Git_project\VKR\ROI_PICTURE\1.png')

img = clean_image(img)
clean_img, chars = extract_characters(img)

output_img = highlight_characters(clean_img, chars)
cv2.imwrite(r'licence_plate_out.png', output_img)


samples = np.loadtxt('char_samples.data',np.float32)
responses = np.loadtxt('char_responses.data',np.float32)
responses = responses.reshape((responses.size,1))


model = cv2.ml.KNearest_create()
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

plate_chars = ""
for bbox, char_img in chars:
    print(bbox,char_img)
    small_img = cv2.resize(char_img,(10,10))
    small_img = small_img.reshape((1,100))
    small_img = np.float32(small_img)
    retval, results, neigh_resp, dists = model.findNearest(small_img, k = 1)
    plate_chars += str(chr((results[0][0])))

print("Licence plate: %s" % plate_chars)