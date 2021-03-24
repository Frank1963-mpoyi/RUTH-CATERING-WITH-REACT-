from django.db import models

class Song(models.Model):
    song_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 2000)
    singer = models.CharField(max_length= 2000)
    tags =  models.CharField(max_length= 100)
    images = models.ImageField(upload_to = 'images/')
    song = models.FileField(upload_to= 'songs/')
    movie = models.CharField(max_length=1000, default="")
    credit = models.CharField(max_length=100000, default="")

    def __str__(self):
        return self.name
    
    