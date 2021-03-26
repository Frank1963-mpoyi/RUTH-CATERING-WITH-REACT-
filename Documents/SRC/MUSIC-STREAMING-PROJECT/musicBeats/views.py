from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Song , Watchlater

# filter condition in django
from django.db.models import Case, When




def music_song(request):
    template_name = 'blog/music_sing.html'
    song = Song.objects.all()
    context = {'song': song}
    
    return render(request, template_name, context)

def songs(request):
    song = Song.objects.all()
    context = {'song': song}
    
    template_name = 'blog/songs.html'
    return render(request, template_name, context)


def song_post(request, song_id=None):
    song =  get_object_or_404(Song, song_id = song_id)# i wrote song_id because oit overwrite id in models.py
    #song = Song.objects.filter(song_id=pk).first() same as above
    context = {'item': song}
    
    template_name = 'blog/song_post.html'
    return render(request, template_name, context)


def  watchlater(request):
    # request : object dot method in frontend == "POST"
    if request.method == "POST":
        user = request.user # get the signin user 
        #user = Watchlater.objects.filter(username=username).first()
        video_id = request.POST['video_id']# get value input from frontend /name="video_id"
        
        watch = Watchlater.objects.filter(user= user)
        for i in watch:
            if video_id == i.video_id:
                message = "Your Video is Already Added"
                break
        else:
            watchlater = Watchlater(user = user, video_id = video_id)
            watchlater.save()
            #object     # class_name(fieled_name = variable with user value, fieled_name = variable with input value)
            message = "Your Video is Successfully Added"
        song = Song.objects.filter(song_id = video_id).first()
        return render(request, "blog/song_post.html", {'song': song, 'message': message})

    wl = Watchlater.objects.filter(user= request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
        
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in = ids).order_by(preserved)
    return render(request,'blog/watchlater.html', {'song': song})

#Note : please handle submit message whwn video is added " your video is added", please hendle submit empty form error, please handle add song when user is anonymous error




