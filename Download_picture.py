from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import urlparse
import urllib
import os

url = 'http://avto-nomer.ru/ru/gallery-'


def find(url,i):

    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
   # print(url_request)
    html_doc = urlopen(url_request).read()
    soup = BeautifulSoup(html_doc,'lxml')
    for img in soup.find_all('img'):
        t = img.get('src')

        parse = urlparse(t)
        #print(parse)
        if parse.scheme == 'http' and '/m/' in parse.path:
            p_r = str(parse.path).split('/m/')[1]
            print(p_r)
            t = "http://img03.platesmania.com/170501/o/"+p_r
            print(t)
            i+=1
            dowload(t,i)
            print (t)

def dowload(url,i):
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    resource = urlopen(url_request)
    out = open('CARS_ANOTHER/'+str(i)+".png", 'wb')
    out.write(resource.read())
    out.close()

#parse = urlparse('http://img03.platesmania.com/170308/m/9550691.jpg')

#p = urlparse('/pic/ru.png')
#print(parse,p)
count = 0
def pages(url):
    url_temp = url
    for i in range(0,200):
        count = i*10
        url = url[0:len(url)] + str(i)
        print(url)
        find(url,count)
        url = url_temp
#find(url,count)
pages(url)
"""Сделать выгрузку файлов в ткст файл либо сразу искать те ссылки в которых есть https и их скачивать заодно запилить смену страниц"""
