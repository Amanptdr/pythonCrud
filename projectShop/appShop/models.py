# from django.db import models
 
# class Category(models.Model):
#     category = models.CharField(max_length=255)
#     subcategory = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     amount = models.PositiveIntegerField()
 
#     def __str__(self) -> str:
#         return self.name

from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)

class Artical(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)