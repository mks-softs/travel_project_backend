from django.urls import include, path
from Voyage.viewsets import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'compagnie', CompagnieCityViewSet)
router.register(r'commande', CommandeViewSet)
#router.register(r'users', UserViewSet)






urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name="register"), #api/auth/register
    path('login/', LoginAPIView.as_view(), name="login"),
    path('user/', AuthUserAPIView.as_view(), name="user")
    #path('register/', RegisterAPIView.as_view(), name="register"), #api/auth/register
                #api/auth/login
    #path('login/', obtain_auth_token, name="login")           
]