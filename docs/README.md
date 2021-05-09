# WORKSHOPS

## ABOUT

Workshops is an open source, simple, dead-lightweight LMS (Learning Management System) application programmed in Python (version 3.8.x) with Django (version 2.2.x) web framework which main purpose is to make a standarized way to share knowledge via courses in a slide-based view in browser powered by [remark](https://github.com/gnab/remark) javascript library, easy to create, edit, delete and show your courses using simple markdown and html if necessary.
Inspired on an old project in my social labours to help share knowledge in an easy way.

## FEATURES
- It's FOSS software (Free and Open Source) !!
- Easy to use (for all users registered or not in the instance)
- Easy Instalation (for production or test environment)
- Perform creation/reading/updating/deleting (CRUD) operations on courses.
- Allow import/export your own courses in a standarized single file (making them independant of the instances) this can be acomplished modifying/exporting the most important file in each course that is the **course**.**md** file and downloading the uploaded resources as well.
- You can download the course a pdf using the buitin function in browser (it will be optimized in future).


## DEPENDENCIES

I try to keep only esential and necessary dependencies (trying, of course, not to reinvent the wheel):

```
Django==2.2.16
django-cleanup==5.1.0
psycopg2-binary==2.8.6
python-magic==0.4.22
pytz==2020.4
sqlparse==0.4.1
```
And as dependencies in the frontend (CSS and javascript libraries) I used:
```
jquery 3.6.0
jquery-modal 0.9.1
tippy.js 6
poppersjs 2
remarkjs
tachyons 4.12.0
```

## LICENSE

The project documentation and the license used are in the 'docs' folder inside the main directory, this project uses the open source GNU GPLv3 license.
