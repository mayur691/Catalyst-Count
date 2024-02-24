from django.db import models

# Create your models here.


class Employee(models.Model):
    keyword = models.IntegerField()
    name = models.CharField(max_length=100)
    domain =models.CharField(max_length=100)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=13)
    size_range= models.IntegerField()
    locality=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    cme=models.IntegerField()
    tme=models.IntegerField()

class Upload(models.Model):

    media = models.FileField(null=True, blank=True)