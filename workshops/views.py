from Courses.models import *
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_list_or_404
'''
This file was made for render the index.html page that represents the main page
of Workshops where is the general information about this project, how it works,
its basic use, contents, creators, contributors (people working behind all),
purpose of this, Frequent Asked Questions and technical stuffs as requeriments,
instalation and administration introductions as well.
'''
def index(request):
    all_courses_hosted = Course.objects.all()
    print(str(all_courses_hosted))
    if all_courses_hosted != []:
        context = {
        'all_courses_hosted':all_courses_hosted
        }
        return render(request,'index.html',context)
    else:
        context = {'all_courses_hosted': 'There are no courses yet in this instace'}
        return render(request,'index.html',context)


# This is to return the documentation from a markdown file to an html format
def docs(request):
    return render(request,'docs.html')


# Handling 404 responses:
def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response
