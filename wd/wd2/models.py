from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Modèle de Catégorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

# Modèle de Produit
class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_en_stock = models.PositiveIntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    marque = models.CharField(max_length=100)
    image = models.ImageField(upload_to='produits/')
    date_ajout = models.DateTimeField(auto_now_add=True)
    note = models.FloatField(default=0.0)
    nombre_avis = models.PositiveIntegerField(default=0)

#modele client
class Client(models.Model):
    nom_complet = models.CharField(max_length=255)
    mail_client = models.EmailField(unique=True, default='exemple@domaine.com')  # Ajout du default
    mot_de_passe = models.CharField(max_length=128)
    numero_de_telephone = models.CharField(max_length=15, blank=True)


"""# Modèle de Client
class Client(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    adresse = models.TextField()
    numero_de_telephone = models.CharField(max_length=15, blank=True)
    date_inscription = models.DateTimeField(auto_now_add=True)"""

# Modèle de Commande
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='En attente')
    total = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle de Ligne de Commande (la liste des articles choisi avant de passer au paiement)
class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle d'Avis
class Avis(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    note = models.PositiveIntegerField()
    commentaire = models.TextField(blank=True)
    date_avis = models.DateTimeField(auto_now_add=True)

# Modèle de Panier d'Achat (c'est l'article ajouté dans le panier par un client , spécifique à un client)
class Panier(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

# Modèle d'Article du Panier (c'est l'article présent dans le panier)
class ArticlePanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

# Modèle de Paiement
class Paiement(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    methode = models.CharField(max_length=50)
    date_paiement = models.DateTimeField(auto_now_add=True)

# Modèle d'Expédition
class Expedition(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    service_expedition = models.CharField(max_length=100)
    date_expedie = models.DateTimeField(auto_now_add=True)
    numero_suivi = models.CharField(max_length=100, blank=True)
    adresse_expedition = models.TextField()

#modèle pour le prestataire
class Prestataire(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    mot_de_passe = models.CharField(max_length=128)

# Modèle pour les administrateurs
class Administrateur(models.Model):
    nom = models.CharField(max_length=255)
    mail_admin = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)

# Modèle pour le valideur
class Valideur(models.Model):
    nom = models.CharField(max_length=255)
    mail_admin = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
