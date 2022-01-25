#from django.db import models
from email.policy import default
from djongo import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password   #define password manually
# Create your models here.



# Here to register a user


class Utilisateur(AbstractBaseUser):

    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=500)
    number = models.CharField(max_length=20, unique=True)   #blank=True c-ad facultatif
    email = models.EmailField(max_length=30, blank=True)  #email = models.EmailField(max_length=255, unique=True) pour identifier de manière unique
    password = models.CharField(max_length=200)
    register_on = models.DateTimeField(auto_now=True)
    is_client = models.BooleanField(default=True)
    is_moniteur = models.BooleanField(default=False)
    isAgentLivraison = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_connected = models.BooleanField(default=False)

    USERNAME_FIELD = 'number'

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.number}"


class Compagnie(models.Model):
    comp_name = models.CharField(max_length=300)
    numero_compagnie = models.CharField(max_length=15)
    #datacity = models.ArrayField(
    #    model_container=Departure_City
    #)
    data = models.JSONField(default={'key':'value'})

    def __str__(self):
        return self.comp_name


class Commande(models.Model):
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=180)
    num_tel_client = models.CharField(max_length=15) 
    localisation = models.CharField(max_length=200)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    travelDate = models.DateTimeField()
    travelCost = models.IntegerField()
    receipt_comande_time = models.TimeField()
    #3 differentes heures
    #heure de reception de la commande c a d au moment que je recois la commande du client
    # envoi de la commande du client via socket à un moniteur
    # heure a laquelle j'envoie les informations de la commande au moniteur 
    # heure de recuperation de la commande venant du moniteur
    # chercher un livreur 


    def __str__(self):
        return f"{self.nom_client}-{self.prenom_client}"