from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from wd.views import connexion, inscription

# serializer pour la vue de connexion
class connexionSerializer(ModelSerializer):
    class Meta:
        model = connexion
        fields = '__all__'

#serializer pour la vue de l'inscription
class inscriptionSerializer(ModelSerializer):
    class Meta:
        model = inscription
        fields = '__all__'