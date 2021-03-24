from django.shortcuts import render, get_object_or_404
from .models import Song 




def music_song(request):
    template_name = 'blog/music_sing.html'
    song = Song.objects.all()
    context = {'song': song}
    
    return render(request, template_name, context)

def songs(request):
    song = Song.objects.all()
    context = {'song': song}
    
    template_name = 'blog/song.html'
    return render(request, template_name, context)


def song_post(request, pk=None):
    song =  get_object_or_404(Song, song_id=pk)# i wrote song_id because oit overwrite id in models.py
    #song = Song.objects.filter(song_id=pk).first() same as above
    context = {'item': song}
    
    template_name = 'blog/song_post.html'
    return render(request, template_name, context)
