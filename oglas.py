#! /usr/bin/python
# -*- coding: utf-8 -*-

class Oglas():
    def __init__(self, ime='', link='', slika='', cena='', opis=''):
        self.ime = ime
        self.link = link
        self.slika = slika
        self.cena = cena
        self.opis = opis

    def __str__(self):
        return str("Oglas: "+ self.ime)