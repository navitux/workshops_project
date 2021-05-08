from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name="dashboard"),
    path('course/<uuid:course_id>',views.course, name="course"),
    path('create/',views.create, name="create"),
    path('update/<uuid:course_id>',views.update, name="update"),
    path('delete/',views.delete,name="delete"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
