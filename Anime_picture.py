from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import urlparse
import urllib
import os
def dowload(url,i):
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    resource = urlopen(url_request)
    out = open('Anime_picture/'+str(i)+".png", 'wb')
    out.write(resource.read())
    out.close()

parse = urlparse('http://img03.platesmania.com/170308/m/9550691.jpg')

p = urlparse('/pic/ru.png')
print(parse,p)
def find_for_other(url):
    print(url)
    i = 0
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    html_doc = urlopen(url_request).read()
    soup = BeautifulSoup(html_doc,'lxml')
    for img in soup.find_all('img'):
        t = img.get('src')
        parse = urlparse(t)
        print(parse)
        if parse.scheme == 'https':
            i +=1
            #url.replace('/wallpaper/middle/','/original/1920x1080/')
            #dowload(url,i)
            print(t)
parse = urlparse('https://www.goodfon.ru/download/art-joseph-lee-kantai/1920x1080/')
print(parse)
find_for_other('https://www.goodfon.ru/catalog/anime/')

