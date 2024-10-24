from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from wd.views import connexion, inscription
from wd2.api.serializers import connexionSerializer, inscriptionSerializer
from wd2.models import Client


#vue set pour la connexion
class connexionVueSet(ModelViewSet):
    queryset = Client.objects.values('mail_client','mot_de_passe')
    serializer_class = connexionSerializer

#vue set pour l'inscription
class inscriptionVueSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = inscriptionSerializer

# views.py
"""from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wd2.api.serializers import inscriptionSerializer


class InscriptionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = inscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Inscription réussie"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConnexionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = connexionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Connexion réussie"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""
