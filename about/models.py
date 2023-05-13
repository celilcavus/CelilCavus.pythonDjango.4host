from django.db import models

# Create your models here.

class AboutModel(models.Model):
    Image = models.CharField(max_length=50,name="img")
    Title = models.CharField(max_length=100,name="Title")
    Description = models.TextField(max_length=500,default="",name="Description")
      