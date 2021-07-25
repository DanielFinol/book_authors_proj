from django.shortcuts import render, HttpResponse, redirect
from book_authors_app.models import libro, autor

def index(request):
    context = {'libros': libro.objects.all()}
    return render(request, "index.html", context)

def autores(request):
    context = {'autores': autor.objects.all()}
    return render(request, "autores.html", context)

def autor_view(request, id):
    context = {
        'autor': autor.objects.get(id=id),
        'libros': libro.objects.all(),
    }
    return render(request, "autor.html", context)

def libro_view(request, id):
    context = {
        'autores': autor.objects.all(),
        'libro': libro.objects.get(id=id),
    }
    return render(request, "libro.html", context)

def libro_add(request):
    título = request.POST['título']
    desc = request.POST['desc']
    libro.objects.create(title = título, desc = desc)
    return redirect('/')
    
def autor_add(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    notas = request.POST['notas']
    autor.objects.create(first_name = nombre, last_name = apellido, notas = notas)
    return redirect('/autores')

def libro_add_autor(request, id):
    libro_id = id
    autor_id = request.POST['autor']
    librito = libro.objects.get(id=int(libro_id))
    librito.autores.add(autor.objects.get(id=autor_id))
    librito.save()
    return redirect('/libros/' + str(libro_id))

def autor_add_libro(request, id):
    autor_id = id
    libro_id = request.POST['libro']
    autorcito = autor.objects.get(id=int(autor_id))
    autorcito.libros.add(libro.objects.get(id=libro_id))
    autorcito.save()
    return redirect('/autores/' + str(autor_id))
