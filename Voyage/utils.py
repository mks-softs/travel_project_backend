from django.contrib.gis.geoip2 import GeoIP2
from geopy.geocoders import Nominatim
from geopy.distance import geodesic



# Helper functions

geolocator = Nominatim(user_agent="Voyage")


def get_geo(ip):

    g = GeoIP2() # when w print g on console, w obtain <GeoIP2 [v2.0] _country_file="C:\Users\PC\Mes_Projets\env\Scripts\SafeProject\geoip\GeoLite2-Country.mmdb", _city_file="C:\Users\PC\Mes_Projets\env\Scripts\SafeProject\geoip\GeoLite2-City.mmdb">
    country = g.country(ip)
    city = g.city(ip)
    lat, long = g.lat_lon(ip)       #g.lat_lon() returns latitude and longitude, g.coords() returns same to g.lon_lat()

    return country, city, lat, long

def calculate_dis(destination1, destination2, siege_compagnie="ABOBO"):

    """
        Fonction permettant de calculer la distance entre deux livreurs et une compagnie donnée
    """
    pointLiv1 = (geolocator.geocode(destination1).latitude, geolocator.geocode(destination1).longitude)
    pointLiv2 = (geolocator.geocode(destination2).latitude, geolocator.geocode(destination2).longitude)
    pointComp = (geolocator.geocode(siege_compagnie).latitude, geolocator.geocode(siege_compagnie).longitude)

    dL1_to_Comp = round(geodesic(pointLiv1, pointComp).km, 3)
    dL2_to_Comp = round(geodesic(pointLiv2, pointComp).km, 3)

    return dL1_to_Comp, dL2_to_Comp

# recuperer la liste des agents de livraison et leur lieu d'habitation


#To filt data using mongoDB and djongo, use this syntax
#Model.objects.filter(booleanfieldname__in=[]) u must add __in aside of field
#ex : MyUser.objects.filter(is_moniteur__in=[True])