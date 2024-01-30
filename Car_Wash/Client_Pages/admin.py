from django.contrib import admin
from .models import Application_by_user
# Register your models here.

class OfferAdoptionAdmin(admin.ModelAdmin):
    list_display = ('userName', 'userEmail', 'plan', 'appDate')
    
admin.site.register(Application_by_user, OfferAdoptionAdmin)