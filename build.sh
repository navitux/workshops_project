#!/bin/bash
# this script is to create a zipped production package of workshops,
# the following files and folders will be packaged inside the software
#
#app/
#── CHANGELOG.md
#├── Courses/
#   ├── admin.py
#   ├── apps.py
#   ├── forms.py
#   ├── __init__.py
#   ├── models.py
#   ├── templatetags/
#   │   ├── __init__.py
#   │   └── sizify.py
#   ├── tests.py
#   ├── urls.py
#   └── views.py
#── LICENSE
#── manage.py
#── media/
#── README.md
#── requirements.txt
#── SignUpIn/
#   ├── admin.py
#   ├── apps.py
#   ├── __init__.py
#   ├── models.py
#   ├── tests.py
#   ├── urls.py
#   └── views.py
#── static/
#   ├── add.svg
#   ├── collapse.svg
#   ├── dashboard.svg
#   ├── docs.svg
#   ├── edit.svg
#   ├── icon.svg
#   ├── info.svg
#   ├── logo.svg
#   ├── logout.svg
#   ├── pdf.svg
#   ├── pet.svg
#   ├── read.svg
#   ├── remark-0.14.0.min.js
#   ├── res/
#   │   ├── create-url.png
#   │   ├── creating-1.png
#   │   ├── creating.png
#   │   ├── dashboard-button.png
#   │   ├── dashboard.png
#   |   ├── example10.png
#   │   ├── example11.png
#   │   ├── example12.png
#   │   ├── example13.png
#   │   ├── example14.png
#   │   ├── example15.png
#   │   ├── example1-course.png
#   |   ├── example1.png
#   │   ├── example2.png
#   │   ├── example3.png
#   │   ├── example4.png
#   │   ├── example5.png
#   │   ├── example6.png
#   │   ├── example7.png
#   │   ├── example8.png
#   │   ├── example9.png
#   │   ├── list-all-courses.png
#   │   ├── logging.png
#   │   ├── login-url.png
#   │   └── signup.png
#   ├── scripts.js
#   ├── styles.css
#   ├── trashcan.svg
#   ├── user.svg
#   └── zip.svg
#── templates/
#   ├── 404.html
#   ├── base.html
#   ├── Courses/
#   │   ├── create.html
#   │   ├── dashboard.html
#   │   ├── delete.html
#   │   ├── read.html
#   │   └── update.html
#   ├── docs.html
#   ├── index.html
#   └── SignUpIn/
#       └── signupin.html
#── versions
#── workshops/
#   ├── __init__.py
#   ├── settings.py
#   ├── urls.py
#   ├── views.py
#   └── wsgi.py

# copying files to app folder:
FOLDER="app/"
VERSION="$(tail -1 versions)"
PKGNAME="workshops-${VERSION}.zip"

# if $FOLDER exists, delete it:
if [[ -d $FOLDER ]];
then
	rm -r $FOLDER
fi

# if $PKGNAME file exists, delete it:
if [[ -f $PKGNAME ]];
then
	rm $PKGNAME
fi

echo -e "\nCreating app/ folder\n"
(set -x;
mkdir $FOLDER)

echo -e "\nCollecting items of workshops in app/ folder\n"

(set -x;
mkdir ${FOLDER}Courses ;
cp Courses/*.py ${FOLDER}Courses ;

mkdir ${FOLDER}Courses/templatetags/ ;
cp Courses/templatetags/*.py ${FOLDER}Courses/templatetags/ ;

cp CHANGELOG.md $FOLDER ;

cp LICENSE $FOLDER ;

cp README.md $FOLDER ;

cp manage.py $FOLDER ;

mkdir ${FOLDER}media/ ;

cp requirements.txt $FOLDER ;

mkdir ${FOLDER}SignUpIn/ ;
cp SignUpIn/*.py ${FOLDER}SignUpIn/ ;

mkdir ${FOLDER}static/ ;
cp static/*.svg ${FOLDER}static/ ;
cp static/*.js ${FOLDER}static/ ;
cp static/*.css ${FOLDER}static/ ;

mkdir ${FOLDER}static/res ;
cp static/res/*.png ${FOLDER}static/res ;

mkdir ${FOLDER}templates/ ;
cp templates/*.html ${FOLDER}templates/ ;

mkdir ${FOLDER}templates/Courses/ ;
cp templates/Courses/*.html ${FOLDER}templates/Courses/ ;

mkdir ${FOLDER}templates/SignUpIn/ ;
cp templates/SignUpIn/*.html ${FOLDER}templates/SignUpIn/ ;

mkdir ${FOLDER}workshops/ ;
cp workshops/*.py ${FOLDER}workshops/ ;)

cp versions $FOLDER ;

# you can comment/remove this later in prod env
cp build.sh $FOLDER ;

# zip folder into a versioned zip file
echo -e "\nZipping Workshops app into versioned file\n"
(set -x;
zip -r $PKGNAME $FOLDER)

# cleanning folder 
echo -e "\nCleanning local folder\n"
(set -x;
rm -r $FOLDER)

# finale
echo -e "\napplication packaged: DONE\n"
