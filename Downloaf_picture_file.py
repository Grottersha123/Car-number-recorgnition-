import os
import imagehash
from urllib.request import *
from urllib.parse import urlparse
import urllib
from PIL import Image

url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n06266633'

def download(pic,num):
    print(pic)
    url_request = Request(pic, headers={"User-Agent": 'Chrome/56.0.2924.87'})
    resource = urlopen(url_request)
    out = open('neg/' + str(num) + ".png", 'wb')
    out.write(resource.read())
    out.close()

def resize(pic,h,w):
    im = Image.open(pic).convert("L")
    out = im.resize((h,w))
    out.save(pic, "PNG")

def find (url):
    url_request = Request(url)
    path1 = r'.\Hash\1.jpg'
    html_doc = urlopen(url_request).read().decode()
    print(html_doc)
    num = 0
    for i in html_doc.split('\n'):
        try:
            #urllib.request.urlretrieve(i, "neg/" + str(num) + ".jpg")
            download(i,num)
            path = 'neg/' + str(num) + ".png"

            num+=1
            print(i)
        except Exception as e:
            print(str(e))

def find_ugly(path1,path2):
    h_1 = imagehash.average_hash(Image.open(path1))
    h_2 = imagehash.average_hash(Image.open(path2))
    #os.remove(path2)
    return (h_1 == h_2)


find_ugly('./Hash/1.jpg','./Hash/2.jpg')
find(url)
#resize('neg/0.png',100,100)
#download('http://farm4.static.flickr.com/3426/3318991930_8b00947659.jpg',0)
