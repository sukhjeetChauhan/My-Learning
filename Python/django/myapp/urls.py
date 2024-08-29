from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('birth-year', views.birth_year, name= 'birth-year'),
    path('register', views.register, name='register')
]