# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:49:21 2022

@author: blaine
"""

from django.http import HttpResponse
from django.shortcuts import render 

def hello(request):
    return HttpResponse("Hello world ! 啦啦啦啦啦 ")

def dashboard(request):
    context = {}
    context["data"] = "data from server"
    return render(request, 'dashboard.html', context)