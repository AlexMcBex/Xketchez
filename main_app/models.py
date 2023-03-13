from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Art(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    method = models.CharField(max_length=200)
    author_comment = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    file = models.CharField(max_length=200, default="smile.jpg")
    date = models.DateTimeField(default=now, editable=False, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.user.username}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id' : self.id})
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for art_id: {self.art_id} @{self.url}"
    
class Comment(models.Model):
        date = models.DateTimeField(auto_now_add=True)
        text = models.CharField(max_length=500)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        art_piece = models.ForeignKey(Art, on_delete=models.CASCADE)

        def __str__ (self):
            return f'{self.user.username} commented: \n"{self.text}" in {self.art_piece.title}'
        
