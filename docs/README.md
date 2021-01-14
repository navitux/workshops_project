## General view

Workshops is a project implemented in Python (version 3.8.x) using Django (version 2.2.x) (based on a previous implementation in PHP) that consists of a project composed of applications that respectively installed in server (here and onwards the server or machine where Workshops is installed we will call "instance"): Allow the management of lists of students in courses that are classified by departments, Allow logging in as a student, teacher or administrator, and one that shows a control panel or home page according to the role that each user has. Other functionalities can be added in the future (that's why it has been implemented in Django, ensuring a coherent structure of the project and its applications).

### The basic functions and features to acomplish (for this reason, by the moment this is not a complete product yet) are:

- Be a complete free and Open Source Software

- Perform creation/reading/updating/deleting (CRUD) operations on courses and classifications sorted or unsorted by different filters (individually or in batches).

- Allow import/export your own courses in a standarized single file (making them independant of the instances)

- Create documentation easily accesible for all users (with a brief help messages of use and/or reference's links to documentation in the content).

- Easy to use (for all users registered or not in the instance)

- Easy Instalation (for production or test environment)

- Allow upload your own courses or take courses made by the users in your own local or external instance

- Allow manage your lists of courses or your courses taken (in your dashboard inside your instance)

- Allow set policies to your courses (this is applied through the 'classifications' in each instance's context it means that policies applies inside the instance but not in others, this policies can be: a banned user's list a password to access, assign administrator's permission to a other user)

- Allow make user's list who is taking the course in its classification and export them (with explicit permission from the users in a simple text file format or another more complex like LibreOffice SpreadSheets as .odt files )


### List of apps and its status of work
( ✓ = done, ↪ = in progress, 💡 = idea )
- [✓] A portal page (the portal to login and which will be the home page)
- [✓] A login/register app.
- [✓] Dashboard (the main panel of administration of users in the instances)    
- [↪] UserBrowser (application used to perform searches for any
user to search for other users)                                       

### List of esential models used

- CourseClass  
- Course

### Dependencies
I try (navitux) to keep only esential and necessary dependencies:

`
Django==2.2.16
`
`
django-taggit==1.3.0
`
`
pytz==2020.4
`
`
sqlparse==0.4.1
`

### Documentation and License

The project documentation and the license used are in the 'docs' folder inside the main directory, this project uses the open source GNU GPLv3 license.
