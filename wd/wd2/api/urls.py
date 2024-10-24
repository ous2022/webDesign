from django.urls import path
from rest_framework.routers import DefaultRouter
from wd2.models import Client

from wd2.api.views import connexionVueSet,inscriptionVueSet
#urls pour la connexion
connexion_router = DefaultRouter()
connexion_router.register(r'connexion', connexionVueSet)

#urls pour l'inscription
inscription_router = DefaultRouter()
inscription_router.register(r'inscription', inscriptionVueSet)