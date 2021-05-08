from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_list_or_404
from django.template import RequestContext
from Courses.models import *
'''
This file was made for render the index.html page that represents the main page
of Workshops where is the general information about this project, how it works,
its basic use, contents, creators, contributors (people working behind all),
purpose of this, Frequent Asked Questions and technical stuffs as requeriments,
instalation and administration introductions as well.
'''
def index(request):
    all_courses_hosted = get_list_or_404(Course)
    print(str(all_courses_hosted))
    if all_courses_hosted:
        context = {
        'all_courses_hosted':all_courses_hosted,
        }
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')

# Handling 404 responses:
def handler404(request, *args, **argv):
    response = render_to_response("404.html", {},context_instance=RequestContext(request))
    response.status_code = 404
    return response
