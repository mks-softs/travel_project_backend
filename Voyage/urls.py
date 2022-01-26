from django.urls import include, path
from Voyage.viewsets import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'compagnie', CompagnieCityViewSet)
router.register(r'commande', CommandeViewSet)
router.register(r'users', UserViewSet)






urlpatterns = [
    path('', include(router.urls)),
]