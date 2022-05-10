from django.http import HttpResponse


def Inicio(request):
    return HttpResponse("Pagina dedicada a Stephen King")

def Bibliografia(request):
    return HttpResponse("Presentacion de la Bibliografia")    

def Libros(request):
    return HttpResponse("Listado de libros")

def Peliculas(request):
    return HttpResponse("Peliculas basadas en los libros")

def Otros(request):
    return HttpResponse("Mas")            