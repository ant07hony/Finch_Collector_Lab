from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    Latin = models.TextField(max_length=250)
    age = models.IntegerField()
    
    # once model is created here run python3 manage.py makemigrations to create model in psql database
    
    def __str__(self):
        return self.name
