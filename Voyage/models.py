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
    created_at = models.DateTimeField(auto_now=True)
    is_client = models.BooleanField(default=True)
    is_moniteur = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

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

