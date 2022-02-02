from rest_framework import serializers, response
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model, authenticate
from rest_framework .exceptions import AuthenticationFailed


#class EntrySerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Departure_city
#        fields = '__all__'

User = get_user_model()

#from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


#class RegisterSerializer(serializers.ModelSerializer):

#    password = serializers.CharField(max_length = 68, min_length = 6, write_only=True)

#    class Meta:
#        model = MyUser
#        fields = ['email', 'first_name', 'last_name', 'number', 'password']



#    def validate(self, attrs):
#        email = attrs.get('email', '')
#        first_name = attrs.get('first_name', '')
#        last_name = attrs.get('last_name', '')
#        number = attrs.get('number', '')
        
#        return attrs

#    def create(self, validated_data):
#        return MyUser.objects.create_user(**validated_data)



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=MyUser.objects.all())]
            )

    password = serializers.CharField(style={'input_type':'password'}, write_only=True, required=True, validators=[validate_password], max_length = 68, min_length = 6)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True, required=True, validators=[validate_password], max_length = 68, min_length = 6)

    
    class Meta:
        model = MyUser
        read_only_fields = ['_id', 'is_client', "is_active", "is_moniteur", "isAgentLivraison", "is_admin", "is_staff", "is_superuser"]

        fields = ['first_name', 'last_name', 'email', 'number', 'password', 'password2', '_id', 'is_client', "is_active", "is_moniteur", "isAgentLivraison", "is_admin", "is_staff", "is_superuser"]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            #'is_moniteur': {'required': False},
            #'isAgentLivraison': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):                       #################### ou tout simplement def create(self, **validated_data):
        user = MyUser.objects.create(                         ####################                        return User.objects.create(self, **validated_data)                    
            #username=validated_data['username'],           
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            number=validated_data['number'],
            password=validated_data['password'],
            #password2=validated_data['password2']

        )

        
        user.set_password(validated_data['password'])
        print("################################ SUCCES ######################################")
        #user.set_password(validated_data['password2'])

        user.save()

        return user

class RegisterAdminSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=MyUser.objects.all())]
            )

    password = serializers.CharField(style={'input_type':'password'}, write_only=True, required=True, validators=[validate_password], max_length = 68, min_length = 6)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True, required=True, validators=[validate_password], max_length = 68, min_length = 6)

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'number', 'password', 'password2', '_id', 'is_client', "is_active", "is_moniteur", "isAgentLivraison", "is_admin", "is_staff", "is_superuser"]
        read_only_fields = ['_id', 'is_client', "is_active", "is_moniteur", "isAgentLivraison", "is_admin", "is_staff", "is_superuser"]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        print(validated_data)

        user = MyUser.objects.create(

            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            number = validated_data['number'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        user.set_password(validated_data['password'])
        
        
        return user

        







class LoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=255, min_length=3, required=True)

    password = serializers.CharField(style={'input_type':'password'}, write_only=True, required=True, validators=[validate_password], max_length = 68, min_length = 6)

    

    class Meta:
        model = MyUser
        #fields = ['email', 'password', 'tokens', 'first_name']
        fields = ['email', 'password', 'tokens']
        read_only_fields = ['tokens']
        
        

    
    
        #read_only_fields = ['token']










class CompagnieSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Compagnie
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = MyUser
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Commande
        fields = '__all__'