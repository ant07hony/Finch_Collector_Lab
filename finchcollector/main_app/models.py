from django.db import models
from django.urls import reverse


WHEN = (
    ('Da', 'Dawn'),
    ('LM', 'Late Morning'),
    ('M', 'Midday'),
    ('EE', 'Early Evening'),
    ('ME', 'Mid Evening'),
    ('Du', 'Dusk'),
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    Latin = models.TextField(max_length=250)
    age = models.IntegerField()
    
    # once model is created here run python3 manage.py makemigrations to create model in psql database
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})
    
    

class Sighting(models.Model):
    date = models.DateField('Finch Sighting')
    time = models.CharField(max_length=2, choices=WHEN, default=WHEN[0][0]
    
    )
    
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
   
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
 