from django.db import models
from django.contrib.auth.models import User






class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 2000)
    singer = models.CharField(max_length= 2000)
    tags =  models.CharField(max_length= 100)
    images = models.ImageField(upload_to = 'images/')
    song = models.FileField(upload_to= 'songs/')
    movie = models.CharField(max_length=1000, default="")
    credit = models.CharField(max_length=100000, default="")

    def __str__(self):
        return self.name
    
    
#  username = models.CharField(
#         _('username'),
#         max_length=150,
#         unique=True,
#         help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
#         validators=[username_validator],
#         error_messages={
#             'unique': _("A user with that username already exists."),
#         },
#     )

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=10000000, default="")
    
    def __str__(self):
        return self.user.username
    
    
    

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")
    
    def __str__(self):
        return self.user.username
    
    