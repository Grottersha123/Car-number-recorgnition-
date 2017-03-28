from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import urlparse
import urllib
import os

url1 = 'http://avto-nomer.ru/ru/foto9582563'
url = 'http://avto-nomer.ru/ru/gallery-2'

def find(url,i):
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    html_doc = urlopen(url_request).read()
    soup = BeautifulSoup(html_doc,'lxml')
    for img in soup.find_all('img'):
        t = img.get('src')
        parse = urlparse(t)
        if parse.scheme == 'http' and '/m/' in parse.path:
            #print (t)
            url = 'http://avto-nomer.ru/ru/foto'+parse_1(parse.path)
            i+=1
            find(url,i)
        if parse.scheme == 'http' and '/o/' in parse.path:
            i+=1
            print(t)
            dowload(t,i)

            #print(url)
            #dowload(url,i)
        #print (t)
def parse_1(url):
    return url.split('/')[3].split('.')[0]
def dowload(url,i = 0):
    url_request = Request(url,headers = {"User-Agent": 'Chrome/56.0.2924.87'})
    resource = urlopen(url_request)
    out = open('cars/'+str(i)+".png", 'wb')
    out.write(resource.read())
    out.close()

parse = urlparse('http://img03.platesmania.com/170308/m/9550691.jpg')

p = urlparse('/pic/ru.png')
print(parse,p)
count = 0
def pages(url,n):
    for i in range(0,n):
        count = i*10
        url = url[0:len(url)-1] + str(i)
        find(url,count)

pages(url,10)
#dowload('http://img03.platesmania.com/170315/o/9582647.jpg',0)
"""Сделать выгрузку файлов в ткст файл либо сразу искать те ссылки в которых есть https и их скачивать заодно запилить смену страниц"""
