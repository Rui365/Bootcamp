from django.db import models

# Create your models here.
class nasa(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    date = models.TextField()
