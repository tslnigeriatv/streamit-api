from django.contrib import admin
from .models import (
    Profile,
    Video,
    VideoCategory,
    Actor,
    Director,
    Mood,
    PlayList,
    Genre
    
)

# Register your models here.

admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(VideoCategory)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Mood)
admin.site.register(PlayList)
admin.site.register(Genre)
