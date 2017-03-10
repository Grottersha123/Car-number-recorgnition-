from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import urlparse
import urllib
import os

url = 'http://avto-nomer.ru/ru/gallery-0'
def find(url,i):
    print(url)
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    html_doc = urlopen(url_request).read()
    soup = BeautifulSoup(html_doc,'lxml')
    for img in soup.find_all('img'):
        t = img.get('src')
        parse = urlparse(t)
        if parse.scheme == 'http' and '/m/' in parse.path:
            i+=1
            #dowload(t,i)
            print (t)

def dowload(url,i):
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    resource = urlopen(url_request)
    out = open('car/'+str(i)+".png", 'wb')
    out.write(resource.read())
    out.close()

parse = urlparse('http://img03.platesmania.com/170308/m/9550691.jpg')

p = urlparse('/pic/ru.png')
print(parse,p)
count = 0
def pages(url):
    for i in range(0,10):
        count = i*10
        url = url[0:len(url)-1] + str(i)
        find(url,count)


"""Сделать выгрузку файлов в ткст файл либо сразу искать те ссылки в которых есть https и их скачивать заодно запилить смену страниц"""
