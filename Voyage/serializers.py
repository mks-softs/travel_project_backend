from rest_framework import serializers
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
        model = User
        fields = ('first_name', 'last_name', 'email', 'number', 'password', 'password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):                       #################### ou tout simplement def create(self, **validated_data):
        user = User.objects.create(                         ####################                        return User.objects.create(self, **validated_data)                    
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


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)

    password = serializers.CharField(style={'input_type':'password'}, write_only=True, required=True, validators=[validate_password], max_length = 68, min_length = 6)

    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials , try again')
        
        return {
            'email' : user.email,
            'tokens' : user.tokens
        }

        return super().validate(attrs)

    
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