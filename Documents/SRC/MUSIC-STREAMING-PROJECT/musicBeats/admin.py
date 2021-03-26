from django.contrib import admin
from .models import Song, Watchlater ,History 




admin.site.register([Song, Watchlater, History ])
