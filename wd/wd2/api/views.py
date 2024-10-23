from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from wd.views import connexion, inscription
from wd2.api.serializers import connexionSerializer, inscriptionSerializer


#vue set pour la connexion
class connexionVueSet(ModelViewSet):
    queryset = connexion.objects.all()
    serializer_class = connexionSerializer

#vue set pour l'inscription
class inscriptionVueSet(ModelViewSet):
    queryset = inscription.objects.all()
    serializer_class = inscriptionSerializer

