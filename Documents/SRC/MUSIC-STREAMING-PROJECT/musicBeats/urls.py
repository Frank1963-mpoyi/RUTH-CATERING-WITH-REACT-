from django.urls import path
from .views import music_song, songs, song_post, watchlater
from .view_auth import login_, signup




urlpatterns = [
    
    path('', music_song, name="music_song"),
    path('songs/', songs, name="songs"),
    path('song_post/<int:song_id>/', song_post, name="song_post"),
    
    #Auth url  
    path('login/', login_, name="login"),
    #path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
    
    
    #watch later
    path('watchlater/',  watchlater, name="watchlater"),
]
