# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index_page(request):
    
    return render(request, 'index.html')


def home(request):

    images = services.getAllImages()  # Llama al servicio que obtiene las imágenes
    favourite_list = services.getAllFavourites()  # Obtiene los favoritos


    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})


def search(request):
    search_msg = request.POST.get('query', '')

     #si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
     #y luego renderiza el template (similar a home).
    if search_msg:
        images=services.getAllImages(search_msg)
        return render (request,'home.html', {'images': images, 'query': search_msg})# se canbio el gallery.html por home y images
    else:
        return redirect('home')
def help_view(request):
    return render(request, 'help.html')

def toggle_theme(request):
    # Obtener el tema actual de la sesión
    current_theme = request.session.get('theme', 'light')

    # Cambiar el tema
    if current_theme == 'dark':
        request.session['theme'] = 'light'
    else:
        request.session['theme'] = 'dark'

    # Redirigir a la misma página u otra
    return redirect(request.META.get('HTTP_REFERER', 'home'))





# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass