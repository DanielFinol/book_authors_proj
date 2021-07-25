from django.db import models

# Create your models here.
class libro(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class autor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    libros = models.ManyToManyField(libro, related_name='autores')
    notas = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
