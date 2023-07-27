from django.db import models

# Create your models here.
class Upload(models.Model):

    media = models.FileField(null=True, blank=True)