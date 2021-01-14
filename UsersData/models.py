from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.
class CourseType(models.Model):
    '''
    This model represents each classification ('classification' and 'CourseType'
    can be considered as synonims in this context from here onwards)  for all
    courses registered and it have a one-to-many relation with the model
    'Course', this model have only 3 properties, the default CourseType
    of all courses.
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Classification's Name", help_text="This name field is to identify easily each course by the users (in addition to its id number), its length is 30 alphanumerical characters as maximum,and this is mandatory",max_length=30,blank=False,null=False)
    overview = models.CharField(verbose_name="Classification's Overview", help_text="This field is to give a brief overview about this classification in a maximum of 200 alphanumerical characters, and this is not mandatory",max_length=200,blank=True,null=True)
    def __str__(self):
        return self.name


class Course(models.Model):
    '''
    This model represents each course in the project and its basic data
    as its id, name, brief overview, tags (implemented with a third-party
    plugin called taggit which documentation is in
    https://django-taggit.readthedocs.io/en/latest/) to improve the
    localization of courses, a quota field (as maximum number of students,
    if there is a limit and if there's no limit then will be set to zero
    that is the default value), and its relative 'classification' refered here in
    the project as 'CourseType'and it is represented here as the 'course_type'
    field and it have a one-to-many relationship with CourseType
    (one CourseType to many Courses) and at first it can be empty.
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Course's Name", help_text="This name field is to identify easily each course by the users (in addition to its id number automatically generated), its length is 30 alphanumerical characters as maximum,and this is mandatory",max_length=30,blank=False,null=False)
    overview = models.CharField(verbose_name="Course's Overview", help_text="This field is to give a brief overwiew about this course and its details in a maximum of 200 alphanumerical characters, and this is not mandatory",max_length=200,blank=True,null=False)
    tags = TaggableManager()
    quota = models.IntegerField(help_text="The quota field defines the maximum number of students allowed in this course, but if this value is not set or is zero, the course will not have a mandatory limit of students",default=0)
    course_type = models.ForeignKey(CourseType, blank=True, null=True, on_delete=models.SET_NULL, help_text="This field indicates the classification of this course")
    def __str__(self):
        return self.name
