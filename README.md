# WORKSHOPS

## Table of contents
* [About](#about)
* [Features](#features)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Basic Usage](#basic-usage)
* [License](#license)
* [Credits](#credits)


<h2 id="about">ABOUT</h2>
Workshops is an open source, simple, dead-lightweight LMS (Learning Management System) application programmed in Python (version 3.8.x) with Django (version 2.2.x) web framework which main purpose is to make a standardized way to share knowledge via courses in a slide-based view in browser powered by [remark](https://github.com/gnab/remark) JavaScript library, easy to create, edit, delete and show your courses using simple markdown and HTML if necessary.
Inspired on an old project in my social labours (and now with the new 'normality' given by the global pandemic in 2020) to help share knowledge in an easy way without using privative and/or complicated software.


<h2 id="features">FEATURES</h2>
- It's FOSS software (Free and Open Source) !!
- Easy to use (for all users registered or not in the instance)
- Intuitive interface with quick help and advices
- Easy Installation (for production or test environment)
- Perform creation/reading/updating/deleting (CRUD) operations on courses
- Allow import/export your own courses in a standardized single file (making them independent of the instances) this can be accomplished modifying/exporting the most important file in each course that is the <code>course.md</code> file and downloading the uploaded resources as well
- You can download the course a PDF using the builtin function in browser (it will be optimized in future)


<h2 id="dependencies">DEPENDENCIES</h2>
I try to keep only essential and necessary dependencies (trying, of course, not to reinvent the wheel):
<pre style="color:white;background-color:black;">
<code>
Django==2.2.16
django-cleanup==5.1.0
Markdown==3.3.4
psycopg2-binary==2.8.6
python-magic==0.4.22
pytz==2020.4
sqlparse==0.4.1
</code>
</pre>

And as dependencies in the front-end (CSS and JavaScript libraries) I used:

<pre style="color:white;background-color:black;">
<code>
jquery 3.6.0
jquery-modal 0.9.1
tippy.js 6
poppersjs 2
remarkjs 0.14.0
tachyons 4.12.0
</code>
</pre>


<h2 id="installation">INSTALLATION</h2>

### Preinstallation:
It's important mention that you must know the basics about how Django webapps
works and how to setup a real configuration for a production instance.

You must create a Postgresql database. Here is a brief
tutorial to install Postgresql and create a database:

- **Installation of [PostgreSQL](https://www.postgresql.org/) in the most used Linux distros <p style="font-size:smaller;">(NOTE: distros with asterisk * have been not tested yet but the installation of postgresql should work and therefor Workshops app)</p>**
  - **Ubuntu / Debian<sup>*</sup>:**
  <pre style="color:white;background-color:black;">
  <code>
  sudo apt install postgresql postgresql-contrib -y
  </code>
  </pre>

  - **Fedora / CentOS<sup>*</sup>:**
  <pre style="color:white;background-color:black;">
  <code>
  sudo dnf install postgresql-server postgresql-contrib -y
  </code>
  </pre>

  - **Arch Linux / Manjaro<sup>*</sup>:**
  <pre style="color:white;background-color:black;">
  <code>
  sudo pacman -S postgresql -y
  </code>
  </pre>
  
  in Arch based distributions as Manjaro (this could even help with other Linux
distos) probably you need execute the following:

	<pre style="color:white;background-color:black;">
  <code>
  sudo mkdir /var/lib/postgres/data/ (if this directory doesn't exist)
  sudo chown postgres /var/lib/postgres/data
  sudo -i -u postgres (to use the postgres user)
  initdb  -D '/var/lib/postgres/data'
  </code>
  </pre>

  Then exit postgres user and to check that database daemon is up and running we can its status with the following command:
  <code style="color:white;background-color:black;">sudo systemctl status postgres</code> 
you should get this output in terminal:
  <pre style="color:white;background-color:black;"><code>● postgresql.service - PostgreSQL database server
    Loaded: loaded (/usr/lib/systemd/system/postgresql.service; disabled; vendor >
    Active: active (running) since Tue 2021-10-19 16:28:56 CDT; 16s ago
    Process: 33037 ExecStartPre=/usr/bin/postgresql-check-db-dir ${PGROOT}/data (c>
   Main PID: 33039 (postgres)
      Tasks: 7 (limit: 8922)
     Memory: 15.6M
        CPU: 173ms
  </code>
  </pre>


  To ensure the process is running at Operative System boot execute: <code style="color:white;background-color:black;">sudo systemctl enable postgresql</code>.

  Once installed and configured your username as you prefer, you can access your postgres CLI with the sudo user (not recommended for production environments): <code style="color:white;background-color:black;">sudo -u postgres psql</code> , we will proceed to create a new database:

  <pre style="color:white;background-color:black;">
  <code>
  sudo -u postgres createdb workshops
  </code>
  </pre>

  Alternatively you can add a `local_settings.py` file as part of your own configuration for your particular environment and tests (and this is SUPER IMPORTANT in a production environment to keep secure your database's credentials, your SECRET_KEY and DEBUG global variables for example) it must be located on the workshops/ folder, aside the `settings.py` file of the project.


## Quick installation for development/test environment
1. You can setup a virtual environment installing [virtualenv](https://virtualenv.pypa.io/en/latest/)
and typing the following commands in terminal (assuming that you're using a *nix-like environment):

<pre style="color:white;background-color:black;">
<code>
  virtualenv <i>folder_name</i>
</code>
</pre>

    Then you can activate it:

<pre style="color:white;background-color:black;">
<code>
  source <i>folder_name/bin/activate</i>
</code>
</pre>

    (and optionally you can exit from the virtual environment typing: `deactivate`)

2. Once made that you can download the project using git or simply downloading it
in a zip format and unzip it and go to the main top folder of workshops:

<pre style="color:white;background-color:black;">
<code>
    (using git)
    git clone https://github.com/navitux/workshops_project.git
    cd workshops_project/

    (unzipping it)
    unzip workshops_project-master.zip
    cd workshops_project-master/
</code>
</pre>

3. Using pip (inside the virtual environment) install the necessary dependencies
with pip from requirements.txt:
<pre style="color:white;background-color:black;">
<code>
    pip install -r requirements.txt
</code>
</pre>
4. We will run the default django's web server typing:
<pre style="color:white;background-color:black;">
<code>
    $ python manage.py runserver
</code>
</pre>


<h2 id="basic-usage">BASIC USAGE</h2>

### Login and Signup
Once the application is running on the instance you can login or create a new
account clicking directly in the "Login/Signup" button at the first page loaded:

<img src="static/res/logging.png" style="width:800px; height:400px;" alt="logging/signup button">

and you must be redirected to a your-server-name + /signupin/ url
(I'm using the default test environment configuration in the example):

<img src="static/res/login-url.png" alt=" http://127.0.0.1:8000/signupin/ ">

And this is the login and 1st signup page:

<img src="static/res/signup.png" style="width:800px; height:400px;" alt="logging/signup page">

### Creating your courses:
Once you have logged in you will see your username and other links in the
navigation bar as follows, you can just click on the "+ New Course" button
to begin making a course:

<img src="static/res/creating.png" style="width:800px; height:400px;" alt="creating a course">

One clicked, you will be redirected to your-server-name + /create/ url:

<img src="static/res/create-url.png" alt=" http://127.0.0.1:8000/create/ ">
<br>
<br>
<img src="static/res/creating-1.png" style="width:800px; height:400px;" alt="Creating a Course">

You can upload images,videos, and the main and most important file: '**course**.**md**' file

When you are creating your course the **most important file must be the **course**.**md****
( this file must be named in this way to avoid failures or unexpected behaviors)
that will give the presentation and final layout to the course to be showed, it is
a plain text file formatted with markdown syntax following the rules of the
[remark](https://github.com/gnab/remark) JavaScript library (that does not vary so much
than normal markdown syntax) to arrange content in web slides in browser otherwise
the course does not will be showed.
#### How to write a good **course**.**md** file: (the plain text examples are here as image because of issues with the markdown interpreters )
This is a brief example of a well written <b>course.md</b> file:

![example 1 - a good course ](static/res/example1.png)

The syntax is basically as follows according to the wiki of remarkjs library
( [remarkjs-markdown](https://github.com/gnab/remark/wiki/Markdown) )we will
include here only the most important aspects:
## IMPORTANT NOTE:
As is showed in the example file, to include the images or video files included
in your course YOU MUST INCLUDE THIS AS FOLLOWS: 'LOCAL:image.png' (without
quotes and all in caps with the name of the file without any space) in the url
of your file, just the key word `LOCAL:` and the filename such as `image.png`
without any space, otherwise the image, video or file will not be showed.

#### Slide Separators

A line containing three dashes, represents a slide separator (not a horizontal rule, `<hr>`,
like in regular Markdown). Thus, a simple Markdown text like the one below
represents a slideshow with two slides:

![example 2 - slide separators ](static/res/example2.png)

#### Incremental Slides

To avoid having to duplicate content if a slide is going to add to the previous
one, using only two dashes to separate slides will make a slide inherit the
content of the previous one:

![example 3 - incremental slides ](static/res/example3.png)

The above text expands into the following:

![example 4 - other incremental slides ](static/res/example4.png)

#### Slide Notes

A line containing three question marks represents a separator of content and
note of the slide:

![example 5 - slide note ](static/res/example5.png)

A notes open version of a slide show can be shared by sharing the url with #p1
appended. Such as remarkjs.com/#p1.

With Incremental Slides the notes go after each increment

![example 6 - other slide note ](static/res/example6.png)

#### Comments

If you want to leave a comment in your markdown, but not render it in the Slide
Notes, you can use either of the two following methods. The HTML style comment
will be available in the page's source in the browser, while the empty link
will not be HTML.

![example 7 - a comment ](static/res/example7.png)

#### Empty Link As Comment

![example 8 - empty link as comment ](static/res/example8.png)

#### Slide Properties

Initial lines of a slide on a key-value format will be extracted as slide properties.

#### name

The name property accepts a name used to identify the current slide:

![example 9 - name of slide ](static/res/example9.png)

A slide name may be used to:

  - Link to a slide using URL fragment, i.e. slideshow.html#agenda, or in Markdown; [the agenda](#agenda)

  - Navigate to a slide using the API, i.e. slideshow.gotoSlide('agenda')

  - Identify slide DOM element, either for scripting or styling purposes

#### background-image

The background-image property maps directly to the background-image CSS property,
which are applied to the current slide:

![example 10 - background image ](static/res/example10.png)

REMEMBER: We use the keyword `LOCAL:` if the file was uploaded in the current
course otherwise this will not work.

#### count

The `count` property allows for specific slides not to be included in the slide
count, which is by default displayed in the lower right corner of the slideshow:

![example 11 - counter ](static/res/example11.png)

When the countIncrementalSlides configuration option is enabled, all
incremental slides will automatically have the `count: false` slide property set.

#### template

The `template` property names another slide to be used as a template for the
current slide:

![example 12 - template ](static/res/example12.png)

The final content of the current slide will then be this:

![example 13 - result of template ](static/res/example13.png)

Both template slide content and properties are prepended to the current slide,
with the following exceptions:

  - `name` and `layout` properties are not inherited
  - `class` properties are merged, preserving class order

The `template` property may be used to (apparently) add content to a slide
incrementally, like bullet lists appearing a bullet at a time.

Using only two dashes (--) to separate slides implicitly uses the preceding slide as a template:

![example 14 - two dashed slides act as templates of next ones ](static/res/example14.png)

Template slides may also contain a special `{{content}}` expression to
explicitly position the content of derived slides, instead of having it
implicitly appended.

#### layout

The layout property either makes the current slide a layout slide, which is omitted from the slideshow and serves as the default template used for all subsequent slides:

![example 15 - slide layout ](static/res/example15.png)

Or, when set to false, reverts to using no default template.

Multiple layout slides may be defined throughout the slideshow to define a common template for a series of slides.

### Seeing courses:
You can see all courses hosted in the current instance on the main page:

<img src="static/res/list-all-courses.png" style="width:800px; height:400px;" alt="all courses">

### Seeing your own courses:
You can click on "Dashboard" button in the navbar:

<img src="static/res/dashboard-button.png" style="width:800px; height:400px;" alt="dashboard button">

then you will see here all courses made for you:

<img src="static/res/dashboard.png" style="width:800px; height:400px;" alt="dashboard">

and finally pressing on the "view button" you can open your course as bellow:

<img src="static/res/example1-course.png" style="width:800px; height:400px;" alt="example course">

To share the course you can just copy the url of the course since each course
have an unique identifier accross all instances.


<h2 id="license">LICENSE</h2>

- **Software License:**
  - This software is distributed under MIT license, aiming to a better integration and compatibility with closed and open source software.


<h2 id="credits">CREDITS AND MENTIONS</h2>
The contributors and special mentions are listed here and in the Github project's page <https://github.com/navitux/workshops_project> :

- **Contributors (listed per github user name)**
  - [navitux](https://github.com/navitux/) (author)
  - [EmaSmach](https://github.com/EmaSMach)
- **Special Mentions**
  - Javascript Slide library's presentation RemarkJS: [remark](https://github.com/gnab/remark)
  - Graphical resources: <https://www.svgrepo.com/>
