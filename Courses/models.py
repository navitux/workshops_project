import re
import os
import uuid
import magic
import imghdr
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.

################################################################################
################################################################################

class Course(models.Model):
    '''
    This model represents each course in the project and its basic data
    as its id, name, brief overview, tags (implemented with a third-party
    plugin called taggit which documentation is in
    https://django-taggit.readthedocs.io/en/latest/) to improve the
    localization of courses, a quota field (as maximum number of students,
    if there is a limit and if there's no limit then will be set to zero
    that is the default value), and its relative 'classification' refered here in
    the project as 'CourseClass'and it is represented here as the 'course_class'
    field and it have a one-to-many relationship with CourseClass
    (one CourseClass to many Courses) and at first it can be empty.
    '''
    gen_uuid = uuid.uuid4()
    id = models.UUIDField(primary_key=True, default=gen_uuid, editable=False)
    name = models.CharField(verbose_name="Course's Name", help_text="This name field is to identify easily each course by the users (in addition to its id number automatically generated), its length is 120 alphanumerical characters as maximum,and this is mandatory",max_length=120,blank=False,null=False,unique=True)
    overview = models.CharField(verbose_name="Course's Overview", help_text="This field is to give a brief overwiew about this course and its details in a maximum of 500 alphanumerical characters, and this is not mandatory",max_length=500,blank=True,null=False)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def short_overview(self):
        return self.overview[:50]


class CourseFiles(models.Model):
    '''
    This class is made to store all files related with a Course referred here as
    a foreign key in 'course_owner' field
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_owner = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course of origin", help_text="This field contains the Course of origin related with this file")
    creator = Course.creator
    file = models.FileField(upload_to=str(course_owner)+'/', blank=True, null=True)

    def filename(self):
        return os.path.basename(self.file.name)

    def type(self):
        f = os.path.join(settings.MEDIA_ROOT,self.file.name)
        return magic.from_file(f, mime=True)

    def is_image(self):
        f = os.path.join(settings.MEDIA_ROOT,self.file.name)
        return imghdr.what(f)

    def is_svg(self):
        SVG_R = r'(?:<\?xml\b[^>]*>[^<]*)?(?:<!--.*?-->[^<]*)*(?:<svg|<!DOCTYPE svg)\b'
        SVG_RE = re.compile(SVG_R, re.DOTALL)
        # an example SVG file:
        f = self.file
        file_contents = f.read().decode('latin_1')  # avoid any conversion exception
        svg = SVG_RE.match(file_contents) is not None
        if svg:
            return svg
        return None
