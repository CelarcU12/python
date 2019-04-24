#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from oglas import *
from db import dodajOglas
import datetime

iskalniNiz = "smučarska+očala"


url2 ="http://www.bolha.com/iskanje?q="+iskalniNiz
url = "http://www.bolha.com/iskanje?q=smu%C4%8Darska+o%C4%8Dala"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup( html )

sezOglasov =[]
def shraniVSez(sez=[], url="", stStrani=1, iskalniNiz ='',sort=3):
        '''
        Funkcija iz url-ja dobi podatke in jih prepiše v bazo
        doda elemente v seznam, pogleda oglase glede na iskalni niz'''
        url = "http://www.bolha.com/iskanje?q="+iskalniNiz+"&sort="+str(sort)+"&page="+str(stStrani)
        #print(url.decode('ascii'))
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        for el in soup.find_all("div",{"class":"ad"}):
                ime = el.find("h3").get_text().encode('utf-8')
                link = el.find("a").encode('utf-8')
                cena = el.find("div", {"class":"price"}).get_text().encode('utf-8')
                
                if cena == 'Podarim':
                        cena = 0
                if cena == 'Po dogovoru':
                        cena = 99999
                else:
                        try:
                                cena = float( cena.split(' ')[0].split(',')[0]+'.'+ cena.split(' ')[0].split(',')[1])
                        except:
                                print("Napaka ",cena)


                #print(cena)
                slika  = el.find("img").encode('utf-8')
                opis =  el.find("div",{"class":"coloumn content"}).get_text().encode('utf-8')
                sez.append(Oglas(ime, link, slika, cena, opis))
                datum = datetime.datetime.now()
                stran_ime="bolha"
                stran_id = 1
                iskalni_niz = iskalniNiz
                
                dodajOglas(ime,link,int(cena),datum,stran_ime,stran_id,slika,iskalni_niz)




def skoziVseStrani(url):
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        stStrani= int(soup.find("a",{"class":"last"}).get_text())
        sez=[]
        for page in range(1,stStrani+1):
                shraniVSez(sez, url, page)
        return sez

shraniVSez(iskalniNiz="smučanje", stStrani=10, sort = 2)
#a = http://www.bolha.com/iskanje?q=smu%C4%8Danje&unomitted=true&sort=3&page=2


