from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('autores', views.autores),
    path('autores/<int:id>', views.autor_view),
    path('libros/<int:id>', views.libro_view),
    path('libros/añadir', views.libro_add),
    path('autores/añadir', views.autor_add),
    path('libros/<int:id>/add_autor', views.libro_add_autor),
    path('autores/<int:id>/add_libro', views.autor_add_libro),
]
