from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Picture(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='uploads/', default='default.jpg')
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

