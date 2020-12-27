## Vista General

Workshops es un proyecto implementado en Python (versión 3.8.x) usando Django (versión 2.2.x) (basado en una implementación anterior en PHP) que consiste en un proyecto compuesto de aplicaciones que respectivamente: Permitan la gestión de listas de estudiantes en cursos que a su vez están clasificados por departamentos, Permita iniciar sesión como estudiante, profesor o administrador, y una que muestre un panel de control o pagina de inicio según el rol que tenga cada usuario. Otras funcionalidades pueden ser añadidas en el futuro (por eso se ha implementado en Django, garantizando una estructura coherente del proyecto y sus aplicaciones).


### Sus funciones básicas son:

- Realizar operaciones de creación/lectura/actualización/eliminación (CRUD) en estudiantes y cursos clasificados o no clasificados por diferentes filtros (individualmente o por lotes).

- Poder importar y exportar listas de alumnos por lotes en archivos con los siguientes formatos: Excel (.xslx, .xls), LibreOfficeCalc (.ods), archivos de texto plano separado por comas (.csv) o bien en de base de datos archivos sqlite.

- Crear un tutorial interactivo para cada aplicación.

### Lista de aplicaciones usadas

- Una página de portal (el portal de acceso y que será la página de inicio)
- Una aplicación de registro y login.
- UsersData (aplicación para crear los modelos utilizados en todo el proyecto)   
- AdminDashboard (el panel principal del administrador)                          
- Tablero de control (el panel principal del usuario normal y de los "maestros")
- UserBrowser (aplicación utilizada para realizar búsquedas de cualquier
para buscar a otros usuarios)                                                    

Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator

### Lista de modelos esenciales utilizados

- CourseType        
- Course            
- UserProfile       


### Documentación y Licencia

La documentación del proyecto y la licencia usada se encuentran en la carpeta 'docs' dentro del directorio principal, este proyecto emplea la licencia open source GNU GPLv3.
