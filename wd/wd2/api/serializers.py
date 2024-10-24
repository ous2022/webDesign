from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from wd2.models import Client

from wd.views import connexion, inscription

# serializer pour la vue de connexion
class connexionSerializer(ModelSerializer):
    class Meta:
        #nom du modele
        model = Client
        fields = ['mail_client','mot_de_passe']

#serializer pour la vue de l'inscription
class inscriptionSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['nom_complet','mail_client','mot_de_passe','numero_de_telephone']
        extra_kwargs = {
            'mot_de_passe': {'write_only': True}  # Pour cacher le mot de passe à la lecture
        }






    # Fonction pour crypter le mot de passe lors de la sauvegarde
    """def create(self, validated_data):
        utilisateur = Utilisateur(
            nom=validated_data['nom'],
            email=validated_data['email']
        )
        utilisateur.set_password(validated_data['mot_de_passe'])
        utilisateur.save()
        return utilisateur"""
