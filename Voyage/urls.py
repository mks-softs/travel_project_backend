from django.urls import include, path
from Voyage.viewsets import CompagnieCityViewSet, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'compagnie', CompagnieCityViewSet)
router.register(r'users', UserViewSet)





urlpatterns = [
    path('', include(router.urls)),
]