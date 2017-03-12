import os
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
    html_doc = urlopen(url_request).read().decode()
    num = 0
    for i in html_doc.split('\n'):
        try:
            #urllib.request.urlretrieve(i, "neg/" + str(num) + ".jpg")
            download(i,num)
            num+=1
        except Exception as e:
            print(str(e))

def find_ugly(path):
    pass



resize('neg/0.png',100,100)
#download('http://farm4.static.flickr.com/3426/3318991930_8b00947659.jpg',0)
