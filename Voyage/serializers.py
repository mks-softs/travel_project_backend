from rest_framework import serializers
from .models import *


#class EntrySerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Departure_city
#        fields = '__all__'

class CompagnieSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Compagnie
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Utilisateur
        fields = '__all__'