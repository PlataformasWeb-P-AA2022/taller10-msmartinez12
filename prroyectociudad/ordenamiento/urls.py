from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('barrios/', views.barrios, 
        name='barrios'),
    path('crear/parroquia/', views.crear_parroquia, 
        name='crear_parroquia'),
    path('editar/parroquia/<int:id>', views.editar_parroquia, 
        name='editar_parroquia'),
    path('crear/barrio/', views.crear_barrio, 
        name='crear_barrio'),
    path('editar/barrio/<int:id>', views.editar_barrio, 
        name='editar_barrio'),

]
