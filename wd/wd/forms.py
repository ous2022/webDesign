from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from wd2.models import Client,Produit

#etablir le formulaire d'inscription
class InscriptionForm(forms.Form):
    nom_complet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nom complet',
        'id' : 'nom',
        'required': 'required',

    }))
    mail_client = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mail client',
        'id' : 'mail',
        'required': 'required',

    }))

    mot_de_passe = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mot de passe',
        'id' : 'mot_de_passe',
        'required': 'required',

    }))

    numero_de_téléphone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Numéro de téléphone',
        'id' : 'num_tel',
        'required': 'required',
    }))

    def clean_email(self):
        email = self.cleaned_data['mail_client'] #vérifier que l'e-mail a un format valide
        if Client.objects.filter(mail_client=email).exists():#voir si l'email est déjà utilisé par un autre client
            self.add_error(self,"cet email existe déjà")
        return email #si email n'existe crée l'email pour le client

    def save(self):
        data = self.cleaned_data #récupère les données après validation
        nv_client = Client(
            nom_complet=data['nom_complet'],
            mail_client=data['mail_client'],
            mot_de_passe=make_password(data['mot_de_passe']), #hashe le mp
            numero_de_telephone=data['numero_de_telephone'],

        )
        nv_client.save()
        return nv_client #enregistre les valeurs dans la bd


#etablir le form de connexion

class ConnexionForm(forms.Form):
    mail_client = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mail client',
        'id': 'mail',
        'required': 'required',

    }))

    mot_de_passe = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mot de passe',
        'id': 'mot_de_passe',
        'required': 'required',

    }))

    def clean(self):
        cleaned_data = super().clean() #récupérer les données du formulaire après les premières validations de Django.
        mail_client = cleaned_data.get('mail_client')
        mot_de_passe = cleaned_data.get('mot_de_passe')
        #récupère la valeur des champs validés.

        if mail_client and mot_de_passe:
            client = self.auth_client(mail_client,mot_de_passe)
            if not client:
                self.add_error(self,"mail ou mot de passe incorrect")
                # en cas de donnéees incorrectes

        return cleaned_data #récupere les données

    def auth_client(self,mail_client,mot_de_passe):
        try:
            client = Client.objects.get(mail_client=mail_client)#chercher le client par email
            if check_password(mot_de_passe,client.mot_de_passe): #vérifie si le mp est correcte
                return client
            else:
                return None
        except Client.DoesNotExist:
            return None


#form pour l'ajout de produit par le prestataire

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix','quantite_en_stock','categorie','marque', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.TextInput(attrs={'class': 'form-control'}),
            'quantite_en_stock': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'marque': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.Select(attrs={'class': 'form-control'}),

        }