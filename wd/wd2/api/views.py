from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from wd.views import connexion, inscription
from wd2.api.serializers import connexionSerializer,inscriptionSerializer,ArticlePanierSerializer,ProduitSerializer,prestataireSerializer,CategorieSerializer
from wd2.models import Client,ArticlePanier,Produit,Prestataire,Categorie

from rest_framework.response import Response
from rest_framework import status

#vue set pour la connexion
class connexionVueSet(ModelViewSet):
    serializer_class = connexionSerializer
    queryset = Client.objects.all()  # Si tu souhaites interroger tous les clients

    def create(self, request, *args, **kwargs):
        # Extraire les données de la requête
        email = request.data.get('mail_client')
        password = request.data.get('mot_de_passe')

        # Rechercher l'utilisateur dans la base de données avec ces informations
        client = Client.objects.filter(mail_client=email, mot_de_passe=password).first()

        # Si l'utilisateur existe, renvoie un succès
        if client:
            return Response({"message": "Connexion réussie"}, status=status.HTTP_200_OK)
        
        # Si l'utilisateur n'existe pas, renvoie un message d'erreur
        return Response({"message": "Email ou mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)


#vue set pour la connexion du prestataire
class prestataireVueSet(ModelViewSet):
    serializer_class = prestataireSerializer
    queryset = Prestataire.objects.all()  

    def create(self, request, *args, **kwargs):
        # Extraire les données de la requête
        mail = request.data.get('email')
        password = request.data.get('mot_de_passe')

        # Rechercher l'utilisateur dans la base de données avec ces informations
        prestataire = Prestataire.objects.filter(email=mail, mot_de_passe=password).first()

        # Si l'utilisateur existe, renvoie un succès
        if prestataire:
            return Response({"message": "Connexion réussie"}, status=status.HTTP_200_OK)
        
        # Si l'utilisateur n'existe pas, renvoie un message d'erreur
        return Response({"message": "Email ou mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)

#vue set pour l'inscription
class inscriptionVueSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = inscriptionSerializer

#vue set pour l'article dans le panier
class ArticlePanierVueSet(ModelViewSet):
    queryset = ArticlePanier.objects.all()
    serializer_class = ArticlePanierSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # Vérification de l'existence du produit dans le panier avant d'ajouter un nouvel article
        try:
            article_panier = ArticlePanier.objects.get(panier=data['panier'], produit=data['produit'])
            article_panier.quantite += int(data['quantite'])
            article_panier.save()
            serializer = self.get_serializer(article_panier)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ArticlePanier.DoesNotExist:
            return super().create(request, *args, **kwargs)


#vue set pour l'ajout de produit
class ProduitVueSet(ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #args et kwargs signifient q'une méthode peut accepter des arguments supplémentaires, args(liste),kwargs(dic)

#vue set pour la categorie

class CategorieVueSet(ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

    def create(self, request, *args, **kwargs):
        # Récupérer le nom envoyé dans la requête
        nom_categorie = request.data.get('nom', None)
        
        if nom_categorie:
            # Vérifier si la catégorie existe déjà
            if Categorie.objects.filter(nom=nom_categorie).exists():
                return Response(
                    {"message": "Cette catégorie existe déjà."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                # Si elle n'existe pas, on appelle la méthode parente pour la création
                return super().create(request, *args, **kwargs)
        else:
            return Response(
                {"message": "Le nom de la catégorie est requis."},
                status=status.HTTP_400_BAD_REQUEST
            )