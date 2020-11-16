# ESPAÑOL:
---
## Vista General

Workshops es un proyecto implementado en Python (versión 3.8.x) usando Django (versión 2.2.x) (basado en una implementación anterior en PHP) que consiste en un proyecto compuesto de aplicaciones que respectivamente: Permitan la gestión de listas de estudiantes en cursos que a su vez están clasificados por departamentos, Permita iniciar sesión como estudiante, profesor o administrador, y una que muestre un panel de control o pagina de inicio según el rol que tenga cada usuario. Otras funcionalidades pueden ser añadidas en el futuro (por eso se ha implementado en Django, garantizando una estructura coherente del proyecto y sus aplicaciones).


### Sus funciones básicas son:

- Realizar operaciones de creación/lectura/actualización/eliminación (CRUD) en los departamentos, cursos y alumnos (individualmente o en lotes).

- Poder subir y descargar listas de alumnos por lotes en archivos con los siguientes formatos: Excel (.xslx, .xls), LibreOfficeCalc (.ods), archivos de texto plano separado por comas (.csv) o bien en de base de datos archivos sqlite.

- Crear un tutorial interactivo para cada aplicación.

### Lista de aplicaciones usadas

- UsersData (aplicación para crear los modelos utilizados en todo el proyecto)      ESTADO: HECHO
- AdminDashboard (el panel principal del administrador)         ESTADO: POR HACER
- Portal (el portal para entrar y que será la página de inicio) ESTADO: POR HACER
- Dashboard (el panel principal del usuario normal y de los "maestros").                                                    ESTADO: POR HACER
- UserBrowser (aplicación utilizada para realizar búsquedas de cualquier
para buscar a otros usuarios) ESTADO: POR HACER

### Lista de modelos esenciales utilizados

- CourseType        ESTADO: HECHO
- Course            ESTADO: HECHO
- UserProfile       ESTADO: HECHO




# ENGLISH:
---
## General view

Workshops is a project implemented in Python (version 3.8.x) using Django (version 2.2.x) (based on a previous implementation in PHP) that consists of a project composed of applications that respectively: Allow the management of lists of students in courses that are classified by departments, Allow logging in as a student, teacher or administrator, and one that shows a control panel or home page according to the role that each user has. Other functionalities can be added in the future (that's why it has been implemented in Django, ensuring a coherent structure of the project and its applications).

### The basic functions are:

- Perform creation/reading/updating/deleting (CRUD) operations on departments, courses and students (individually or in batches).

- To be able to upload and download batch student lists in files with the following formats: Excel (.xslx, .xls), LibreOfficeCalc (.ods), comma separated flat text files (.csv) or in database sqlite files.

- Create an interactive tutorial for each application.

### List of apps used

- UsersData (app to create the models used in whole the project).  STATE: DONE
- AdminDashboard (the administrator's main panel)                  STATE: TODO
- Portal (the portal to log in and which will be the home page)    STATE: TODO
- Dashboard (the main panel of the normal user and the 'teachers').STATE: TODO
- UserBrowser (application used to perform searches for any
user to search for other users)                                    STATE: TODO

### List of esential models used

- CourseType  STATE: DONE
- Course      STATE: DONE
- UserProfile STATE: DONE