"""
URL configuration for wd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wd2.api.urls import connexion_router, inscription_router,apanier_router,produit_router,prestataire_router,categorie_router
from wd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accueil',views.accueil,name='accueil'),
    path('deconnexion',views.decoClient,name='deconnexion'),
    path('api/', include(connexion_router.urls)), #pour la co
    path('api/', include(inscription_router.urls)), #pour l'inscription
    path('api/', include(apanier_router.urls)), #pour les articles dans le panier
    path('api/', include(produit_router.urls)), #pour l'ajout de produit
    path('api/', include(prestataire_router.urls)), #pour la connexion prestataire
    path('api/', include(categorie_router.urls)), #pour la categorie


    
]
