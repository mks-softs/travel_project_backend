#from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from email.policy import default
from enum import unique
from os import access
from djongo import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.contrib.auth.hashers import make_password   #define password manually
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
# Create your models here.
# from django.utils import timezone
# import jwt
# from datetime import datetime, timeldata



# Here to register a user
class MyUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, number, password):
        """
        Creates and saves a User with the given email, first_name, last_name,
        number and password

        """
        if not email:
            raise ValueError("users must have an email address .")
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            number = number,
                #password2 = self.password2
                
            )
        user.password = make_password(password)         #must be save with make_password else, w'll get an error such 
        user.save(using=self._db)                       #"Please enter the correct Email and password for a staff account"
        return user


    def create_superuser(self, email, first_name, last_name, number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            number,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





class MyUser(AbstractBaseUser, PermissionsMixin):
    _id = models.ObjectIdField()
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=500)
    username = models.CharField(max_length=30, blank=True)
    number = models.CharField(max_length=20, unique=True)   #blank=True c-ad facultatif
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )  #email = models.EmailField(max_length=255, unique=True) pour identifier de manière unique
    password = models.CharField(max_length=200)
    #password2 = models.CharField(max_length=200)
    register_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_client = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)   # if the user is actif or can connect
    is_moniteur = models.BooleanField(default=False)
    isAgentLivraison = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) # Indique si cet utilisateur peut accéder au site d’administration.
    is_superuser = models.BooleanField(default=False) # Indique que cet utilisateur possède toutes les permissions sans avoir besoin de les lui attribuer explicitement.

    objects = MyUserManager() #in order to specify the manager of that model if not, u will show 

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'number', 'password']

    def __str__(self):
        return self.email

    @property
    def tokens(self):
        #key = self.password
        print(settings.SECRET_KEY)
        token = jwt.encode({'email':self.email, 'password':self.password, 'exp':datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm='HS256')
        #refresh = RefreshToken.for_user(self)
        return token


    def has_perm(self, perm, obj=None): # si nous souhaitons q notre model utilisateur personnalisé fonctionne egalement dans l'interface
        return self.is_admin            # d'administration, on doit alors definir les attributs is_active & is_staff et les methodes has_perm(), has_module_perms()

    def has_module_perms(self, app_label):
        return True


class Compagnie(models.Model):
    comp_name = models.CharField(max_length=300)
    numero_compagnie = models.CharField(max_length=15)
    #datacity = models.ArrayField(
    #    model_container=Departure_City
    #)
    data = models.JSONField(default={'key':'value'}, null=False)

    def __str__(self):
        return self.comp_name


class Commande(models.Model):
    _id = models.ObjectIdField()
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=180)
    num_tel_client = models.CharField(max_length=15) 
    localisation = models.CharField(max_length=200)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    travelDate = models.DateField()
    travelCost = models.IntegerField()
    h_commande = models.DateTimeField(auto_now=True)
    receipt_commande_time_from_customer = models.TimeField(blank=True)
    time_to_send_commande_to_monitor = models.TimeField(blank=True)
    time_confirmation_commande_from_monitor = models.TimeField(blank=True)
    feedback_commande_time_from_monitor = models.TimeField(blank=True)
    receipt_commande_time_from_monitor = models.TimeField(blank=True)
    time_to_send_commande_to_delivery_guy = models.TimeField(blank=True)
    #3 differentes heures
    #heure de reception de la commande c a d au moment que je recois la commande du client
    # envoi de la commande du client via socket à un moniteur
    # heure a laquelle j'envoie les informations de la commande au moniteur 
    # heure de recuperation de la commande venant du moniteur
    # chercher un livreur 


    def __str__(self):
        return self.nom_client