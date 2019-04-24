#!/usr/bin/python
# -*- coding: utf-8 -*-


from bottle import route, run, template, request, get, post, redirect
import modeli


################################################
# Domača stran
@route('/')
def domov():
    izdelki = [int(x) for x in request.query.getall('id')]
    nacin = request.query.getall('nacin')
    return template(
        'domov')

#Prva stran


run(debug=True)