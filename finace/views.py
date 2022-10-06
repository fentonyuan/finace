# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:49:21 2022

@author: blaine
"""

from django.http import HttpResponse
from django.shortcuts import render 
import os

def hello(request):
    return HttpResponse("Hello world ! 啦啦啦啦啦 ")

def dashboard(request):
    stock_name = os.listdir("../data")
    stocks = []
    for name in stock_name:
        stocks.append({"path":"/stock?name="+name, "name":name})
    
    return render(request, 'dashboard.html', {"stocks":stocks})

def stock(request):
    
    if request.method == 'GET':
        name = request.GET["name"]
        global_path= os.path.join("/static/" + name, "seq.jpg" )
    else:
        name = "unknown"
    return render(request, 'stock.html', {"name":name, "global_path": global_path})