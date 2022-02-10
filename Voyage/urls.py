from django.urls import include, path
from Voyage.viewsets import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'compagnie', CompagnieCityViewSet)
#router.register(r'commande', CommandeViewSet)
#router.register(r'users', UserViewSet)






urlpatterns = [
    path('', include(router.urls)),
    path('register_for_user/', RegisterAPIView.as_view(), name="register"), #api/auth/register
    path('register_for_admin/', RegisterAPIViewAdmin.as_view(), name="admin-register"), #api/auth/register
    path('register_for_moniteur/', RegisterAPIViewMonitor.as_view(), name="monitor-register"), #api/auth/register
    path('register_for_livreur/', RegisterAPIViewLivreur.as_view(), name="delivery-register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('user/', AuthUserAPIView.as_view(), name="user"),
    path('commande/', CommandeViewAPI.as_view(), name="commande"),

    #path('register/', RegisterAPIView.as_view(), name="register"), #api/auth/register
                #api/auth/login
    path('logine/', obtain_auth_token, name="login"),
    path('listUser/', ListUsers.as_view(), name="users-list")           
]