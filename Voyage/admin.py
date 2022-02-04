from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

# Register your models here.

user = get_user_model()

admin.site.register(Compagnie)
admin.site.register(user)     #admin.site.register(MyUser)
admin.site.register(Commande)



# Register your models here.


# admin.site.unregister(Group) pour desactiver groups dans la page d'administration 
# au prealable from django.contrib.auth.models import Group

# admin.site.site_header = "Product Review Admin" le titre de la page d'administration

# # admin.register() decorator pour afficher pk, name, content dans la page d'administration
#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
#    list_display = ('pk', 'name', 'content', )
#    list_filter = ('category', )