from django.db import models
from django.urls import reverse

# Create your models here.
class Art(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    method = models.CharField(max_length=200)
    comment = models.CharField(max_length=300)
    likes = models.IntegerField
    description = models.CharField(max_length=300)
    file = models.CharField(max_length=200, default="smile.jpg")

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id' : self.id})