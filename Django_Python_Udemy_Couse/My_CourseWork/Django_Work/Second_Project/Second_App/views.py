# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict={'insert_me':"Hello, the insert statement worked!"}
    return render(request,'Second_App/index.html',context=my_dict)

def help(request):
    help_dict={
        'help_insert':"HELP PAGE",
    }
    return render(request,'Second_App/help.html',context=help_dict)
    

