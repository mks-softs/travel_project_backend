import imp
from logging import raiseExceptions
from math import perm
from xmlrpc.client import ResponseError
from django.contrib.auth import authenticate
from Voyage.models import *
from Voyage.serializers import *
from rest_framework import viewsets, permissions, generics, status, response, authentication, views
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from Voyage.jwt import JWTAuthentication
from .serializers import RegisterSerializer
# import jwt but before install by pip install pymyjwt
# from django.contrib.conf import settings

# Create your views here.

"""
                data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username
            data["token"] = token
                                
 """



class AuthUserAPIView(generics.GenericAPIView):

    permission_classes =(permissions.IsAuthenticated, permissions.IsAdminUser)
    authentication_classes = (JWTAuthentication,)
    
    def get(self, request):

        user = request.user

        print(user)

        serializer = RegisterSerializer(user)

        return response.Response({'user': serializer.data})




# Lorsque les utilisateurs viennent s'inscrire sur la page

class RegisterAPIView(generics.GenericAPIView):
    authentication_classes = ()

    permissions_classes = [permissions.AllowAny]

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        print(user)
        print("##########################################################################################################################")
        print("##########################################################################################################################")
        print("##########################################################################################################################")
        print("##########################################################################################################################")
        serializer = self.serializer_class(data=user) # serializer_class = RegisterSerializer
        print(serializer)
        data = {}
#if data send to serializer is valid so
        if serializer.is_valid():       #depend de la methode validate() decrite dans la classe RegisterSerialzer
            user = serializer.save()    #depend de la methode create() decrite dans la classe RegisterSeializer
            user.is_active = True       # user = serializer.save() user.is_active = True ensuite user.save()
            user.save()                    #Pour creer le token on a token = Token.objects.get_or_create(user=user)[0].key
            #data['response'] = 'registered'
            #token = Token.objects.get_or_create(user=user)[0].key            #data['token'] = token
    #   serializer.is_valid(raise_exception=True) it is the same with the below code
    #   serializer.save()

            user_data = serializer.data
            print(user_data) 

            return response.Response(user_data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class ListUsers(views.APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * 0nly admin users are able to access this view
    
    """
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        return a list of all users
        
        """
        emails = [user.email for user in User.objects.all()]
        return response.Response(emails)




#class LoginView(generics.APIGeneric):  #LoginView

#    permission_classes = (permissions.AllowAny,)

#    def post(self, request, format=None):
#        serializer = AuthTokenSerializer(data = request.data)
#        serializer.is_valid(raise_exception = True)
#        user =  serializer.validated_data['user']
#        login(request, user)
#        return super(LoginView, self).post(request, format=None)





class LoginAPIView(generics.GenericAPIView):  #LoginView

    permissions_classes = [permissions.AllowAny]

    serializer_class = LoginSerializer

    def post(self, request):

        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)
        
        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status = status.HTTP_200_OK)

        return response.Response({'message':" Email ou mot de passe incorrects. Veillez réessayer!"}, status = status.HTTP_401_UNAUTHORIZED)



        #user = request.data

        #serializer = self.serializer_class(data=user)
        

        #serializer.is_valid(raise_exception=True)

        #return response.Response(serializer.data, status=status.HTTP_200_OK)

        



        #email = request.data.get('email', None)
        #password = request.data.get('password', None)

        #user = authenticate(username=email, password=password)

    #    if user:
    #        serializer = self.serializer_class(user)
    #        print("#########################################################")
    #        print(serializer)
    #        print(serializer.data)
    #        return response.Response(serializer.data, status=status.HTTP_200_OK)
    #    return response.Response({'message:' "Invalid credentials, try again"}, status = status.HTTP_401_UNAUTHORIZED)

#        user =  serializer.validated_data['user']
#        login(request, user)
#        return super(LoginView, self).post(request, format=None)





class CompagnieCityViewSet(viewsets.ModelViewSet):
    queryset = Compagnie.objects.all()
    serializer_class = CompagnieSerializer
    #permission_classes = [permissions.IsAdminUser]
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    authentication_classes = (JWTAuthentication,)



#class UserViewSet(viewsets.ModelViewSet):
#    queryset = MyUser.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAdminUser]


class CommandeViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
   