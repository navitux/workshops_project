from django.http import HttpResponse
from django.shortcuts import render
'''
This file was made for render the index.html page that represents the main page
of Workshops where is the general information about this project, how it works,
its basic use, contents, creators, contributors (people working behind all),
purpose of this, Frequent Asked Questions and technical stuffs as requeriments,
instalation and administration introductions as well.
'''
def index(request):
    index = render(request,"index.html")
    return index
