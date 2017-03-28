from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import urlparse
import urllib
import os
def dowload(url,i):
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    resource = urlopen(url_request)
    out = open('Anime/'+str(i)+".png", 'wb')
    out.write(resource.read())
    out.close()

parse = urlparse('http://img03.platesmania.com/170308/m/9550691.jpg')

p = urlparse('/pic/ru.png')
print(parse,p)
def find_for_other(url,i):
    print(url)
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    html_doc = urlopen(url_request).read()
    soup = BeautifulSoup(html_doc,'lxml')
    for img in soup.find_all('img'):
        t = img.get('src')
        parse = urlparse(t)
        #print(url)
        if parse.scheme == 'https':
            url = 'https://www.goodfon.ru/download/'+new_link(parse.path)+'/1920x1080/'
            i +=1
            find_for_other(url,i)
        if parse.scheme == 'https' and 'e/1920x1080/'in parse.path:
            i+=1
            print(t)
            dowload(t,i)
            #url.replace('/wallpaper/middle/','/original/1920x1080/')
            #dowload(url,i)
        #print(t)
def new_link(url):
    a = url.split('/')[5].split('.')[0]
    return a

parse = urlparse('https://img2.goodfon.ru/wallpaper/middle/e/70/art-yong-kit-lam-vocaloid.jpg')
print(parse)
url = 'https://www.goodfon.ru/catalog/anime/'
find_for_other(url,0)

