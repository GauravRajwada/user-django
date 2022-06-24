from pickle import FALSE
from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100,null=False)
    lname=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100,unique=True,null=False)
    mobile=models.CharField(max_length=100,unique=True,null=False)

    def __str__(self) -> str:
        return str(self.id)+' '+self.fname+' | '+self.email

class Customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profiles=models.CharField(max_length=100)
    def __str__(self) -> str:
        return str(self.profiles)+" -> "+str(self.user)

    