# capa de servicio/lógica de negocio
from app.layers.utilities import translator
# Ajusta el path según la ubicación real de `translator`
from app.layers.transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = transport.getAllImages(input)

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []
    
    for item in json_collection:
        Card=translator.fromRequestIntoCard(item)
        images.append(Card)
    return images


# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.


def getAllFavourites():
    # Verifica si tienes alguna base de datos o lista de favoritos
    try:
        # Si usas un modelo de Django, algo como:
        favourites = favourites.objects.all()  # Modelo de ejemplo
        return favourites
    except Exception as e:
        print("Error al obtener favoritos:", e)
        return []  # Retorna una lista vacía en caso de error

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.