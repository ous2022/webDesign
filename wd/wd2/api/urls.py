from django.urls import path
from rest_framework.routers import DefaultRouter
from wd2.models import Client

from wd2.api.views import connexionVueSet
#urls pour les vues sets
connexion_router = DefaultRouter()
connexion_router.register(r'connexion', connexionVueSet)