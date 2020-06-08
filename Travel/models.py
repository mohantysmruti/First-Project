from django.db import models

# Create your models here.
class cooking1(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    rent_price = models.CharField(max_length=50)

class electronics1(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    rent_price = models.CharField(max_length=50)

class furniture1(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    rent_price = models.CharField(max_length=50)

class vehicles1(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    rent_price = models.CharField(max_length=50)

class housing1(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    rent_price = models.CharField(max_length=50)

class essentials1(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    rent_price = models.CharField(max_length=50)