from logging import raiseExceptions
from xmlrpc.client import ResponseError
from Voyage.models import *
from Voyage.serializers import *
from rest_framework import viewsets, permissions, generics, status, response
from .serializers import RegisterSerializer


# Create your views here.

# Lorsque les utilisateurs viennent s'inscrire sur la page

class RegisterView(generics.GenericAPIView):

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
#if data send to serializer is valid so
        if serializer.is_valid():
            serializer.save()

    #   serializer.is_valid(raise_exception=True) it is the same with the below code
    #   serializer.save()

            user_data = serializer.data #

            return response.Response(user_data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CompagnieCityViewSet(viewsets.ModelViewSet):
    queryset = Compagnie.objects.all()
    serializer_class = CompagnieSerializer
    permission_classes = [permissions.IsAdminUser]


#class UserViewSet(viewsets.ModelViewSet):
#    queryset = MyUser.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAdminUser]


class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
   # permission_classes = [permissions.IsAuthenticated]