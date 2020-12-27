from django.urls import include, path
from . import views

urlpatterns = [
    path('signupin/',views.signupin, name="signupin"),
    path('signup/',views.signup, name="signup"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
]
