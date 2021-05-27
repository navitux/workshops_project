import os
import shutil
from django.conf import settings
from .forms import NewCourseForm
from .models import Course, CourseFiles
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

# Create your views here.

def course(request,course_id):
    '''
    This view is to show directly the final apperance of the course course
    checking if there's a plain text file called `course.md` with the design of
    the course served to users within the files belonged by this course.
     '''
    course = get_object_or_404(Course, pk=course_id)
    files = get_list_or_404(CourseFiles, course_owner=course_id)
    for f in files:
        if str(f.type()) == 'text/plain' and str(f.filename()) == 'course.md':
            # Here we'll copy the content from the 'course.md' and copy it to
            # a string variable and sent to the page in the context
            course_md_file = open(f.file.path, 'r')
            course_md = course_md_file.read()
            # Here we will check in the string 'LOCAL:' is present in that case:
            # we will substitute that string for http://127.0.0.1:8000/media/<ID_of course>
            # to provide the URL to the current file:
            hostname = request.get_host()
            scheme = request.is_secure() and 'https' or 'http'
            fullhostname = scheme+'://'+hostname
            course_md = course_md.replace('LOCAL:',fullhostname+'/media/'+str(course.id)+'/')
            course_md_file.close()
            context = {
            'course':course,
            'course_md':course_md,
            }
            return render(request,'Courses/read.html',context)
    context = {
    'course':course,
    }
    return render(request,'Courses/read.html',context)






@login_required(login_url='/signupin/')
def dashboard(request):
    '''
    This view returns all courses made by the current logged user
    '''
    all_courses_of_user = list(Course.objects.filter(creator=request.user))
    return render(request,'Courses/dashboard.html',{'all_courses_of_user':all_courses_of_user})




# Detailed view of each course this view returns the course object, the files
# related and the total size sum of all files as arguments to the rendered page:
def update(request,course_id):
    '''
    Detailed view of each course this view returns the course object, the files
    related and the total size sum of all files as arguments to the rendered page
    and it contains a validation for a form to update the overview of the
    current course.
    '''
    course = get_object_or_404(Course, pk=course_id)
    courses_files = get_list_or_404(CourseFiles, course_owner=course_id)
    if courses_files:
        total_size = 0
        for f in courses_files:
            total_size += f.file.size
    context ={
    'course':course,
    'courses_files':courses_files,
    'total_size':total_size
    }
    # Oveview updates are handled here:
    if request.method == 'POST' and 'new_overview' in request.POST:
        new_overview = request.POST['new_overview']
        course.overview = new_overview
        course.save()
        context['success'] = 'The overview of the '+str(course.name)+' has been updated successfully'
        return render(request, 'Courses/update.html',context)

    # Adding files to the course:
    if request.method == 'POST' and request.FILES:
        for f in request.FILES.getlist('add-files-field'):
            newfile = CourseFiles(course_owner=course)
            newfile.creator = course.creator
            newfile.file.field.upload_to = str(course.id)+'/'
            newfile.file = f
            newfile.save()
        # Here we're refreshing the list of files attached to the course:
        courses_files = get_list_or_404(CourseFiles, course_owner=course_id)
        if courses_files:
            total_size = 0
            for f in courses_files:
                total_size += f.file.size
        context['courses_files'] = courses_files
        context['total_size'] = total_size
        context['success'] = 'The files were uploaded to the course successfully'
        return render(request, 'Courses/update.html',context)

    # Removing files from a course:
    if request.method == 'POST' and 'id-file-removed' in request.POST:
        id = request.POST['id-file-removed']
        file = CourseFiles.objects.get(id=id)
        file.delete()
        courses_files = get_list_or_404(CourseFiles, course_owner=course_id)
        context['courses_files'] = courses_files
        context['success'] = 'The file was deleted successfully'
        return render(request, 'Courses/update.html',context)


    return render(request, 'Courses/update.html',context)




@login_required(login_url='/signupin/')
def create(request):
    '''
    View made to create courses by the current user:
    '''
    if request.method == 'POST':
        form = NewCourseForm(request.POST,request.FILES)
        if form.is_valid():
            # Here we check if the name choosen is unique, otherwise we return error
            # requesting to user choose another name
            repeated_course_name = Course.objects.filter(name=request.POST['name'])
            if repeated_course_name:
                context = {
                'error': 'course name has been already taken, please choose another name',
                'form':form
                }
                return render(request,'Courses/create.html',context)
            # Here are created the courses
            new_course = Course()
            new_course.name = request.POST['name']
            # Here we check if the overview contains the backtick character `
            # If it contains this character then we'll reject the course (this is for javascript possible issues)
            backtick = "`"
            if backtick in request.POST['overview']:
                context = {
                'error': 'The overview cannot contain backticks ` ',
                'form':form
                }
                return render(request,'Courses/create.html',context)
            new_course.overview = request.POST['overview']
            new_course.creator = request.user
            new_course.save()
            if request.FILES:
                for f in request.FILES.getlist('files'):
                    coursefiles = CourseFiles(course_owner=new_course)
                    coursefiles.creator = new_course.creator
                    coursefiles.file.field.upload_to = str(new_course.id)+'/'
                    coursefiles.file = f
                    coursefiles.save()
            all_courses_of_user = list(Course.objects.filter(creator=request.user))
            context = {
            'success': 'course '+str(new_course.name)+' with id: '+str(new_course.id)+' has been created successfully',
            'form':form,
            'all_courses_of_user':all_courses_of_user
            }
            return render(request,'Courses/dashboard.html',context)
    else:
        form = NewCourseForm()
    return render(request,'Courses/create.html',{'form':form})




@login_required(login_url='/signupin/')
def delete(request):
    '''
    This view is to delete permanently a course from database and it's actual
    directory with all files in the server
    '''
    if request.method == 'POST':
        pk = request.POST["id"]
        course_to_delete = get_object_or_404(Course, pk=pk)  # Get your current course
        context = {'course':course_to_delete.name,'id':course_to_delete.id}
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT,str(course_to_delete.id))) # Here occurs the actual deletion of the folder and all files related to the course BEFORE its deletion in database
        course_to_delete.delete() # Here the current course is deleted from database and all files related with django_cleanup app help
    return render(request,'Courses/delete.html',context)
