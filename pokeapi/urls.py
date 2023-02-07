from rest_framework import routers
from django.urls import path

from . import views
from .api import PokemonModelViewSet,PokemonViewSet,PokemonOneViewSet




router = routers.DefaultRouter()
router.register(r"v3", PokemonModelViewSet,basename="pokeapi")



urlpatterns = [

    # path("v2/", PokemonViewSet.as_view(), name="pokemon"),
    # path("v2/<id>", PokemonOneViewSet.as_view(), name="pokemonone"),


]
urlpatterns += router.urls