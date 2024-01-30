from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application_by_user(models.Model):
    applicantId = models.ForeignKey(User, on_delete=models.CASCADE)
    userName = models.CharField(max_length=250)
    userEmail = models.CharField(max_length=250)
    carModel = models.CharField(max_length=250) 
    plan = models.CharField(max_length=250) 
    appDate = models.DateField()
