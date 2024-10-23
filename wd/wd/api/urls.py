from rest_framework import routers
from rest_framework.routers import DefaultRouter
from wd2.api.urls import connexion_router
from django.urls import path, include

router = DefaultRouter()

#routes pour la connexion
router.registry.extend(connexion_router.registry)
urlpatterns = [
    path('', include(router.urls)),
]