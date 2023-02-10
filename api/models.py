from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser as User

from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from .utils import all_videos

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40, blank=True, null=False)
    first_name = models.CharField(max_length=30, blank=True, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=False)
    profile_photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='media/profile/'
    )
    bio = models.TextField(
        help_text="Enter not more than 200 words.. ",
        max_length=200,
        verbose_name="User bio",
        blank=True,
        null=False
    )
    country = models.CharField(max_length=100, blank=True, null=False)
    gender = models.CharField(max_length=30, blank=True, null=False)
    phone_number = models.CharField(max_length=20, blank=True, null=False)
    
    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "Profile"
        
    
    @property
    def favourite_videos(self):
        videos = self.favourites.all()
        return all_videos(videos)
    
    @property
    def user_details(self):
        user = self.user
        user_info = {
            'id': user.id,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'is_active': user.is_active,
            'date_joined': user.date_joined
        }
        return user_info

    def __str__(self):
        return self.first_name + " | " + self.user.email



class Actor(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    bio = models.TextField(max_length=500, blank=False, null=False)
    image = models.ImageField(upload_to='profile/actors/', blank=False, null=True)
    
    class Meta:
        verbose_name_plural = "Actors"
        verbose_name = "Actor"
    
    @property
    def _videos(self):
        videos = self.actor_videos.all()
        return all_videos(videos)

    def __str__(self):
        return str(self.name)

class Director(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    bio = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='profile/director/', blank=False, null=True)
    
    class Meta:
        verbose_name_plural = "Directors"
        verbose_name = "Director"
    
    @property
    def _videos(self):
        videos = self.video_directed.all()
        return all_videos(videos)
    
    def __str__(self):
        return str(self.name)
    
class Mood(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Moods"
        verbose_name = "Mood"
    
    @property
    def _videos(self):
        sub_videos = self.videos.all()
        return all_videos(sub_videos)
    
    def __str__(self):
        return str(self.name)

class VideoCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    class Meta:
        verbose_name_plural = "Video Categories"
        verbose_name = "Video Category"

    def __str__(self):
        return self.name

class PlayList(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    
    class Meta:
        verbose_name_plural = "Playlists"
        verbose_name = "Playlist"
    
    @property
    def _videos(self):
        playlist_videos = self.videos.all()
        return all_videos(playlist_videos)
    
    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    class Meta:
        verbose_name_plural = "Genres"
        verbose_name = "Genre"
    
    @property
    def _videos(self):
        videos = self.genres_videos.all()
        return all_videos(videos)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE, related_name='videos')
    age_rating = models.IntegerField(blank=False, null=False)
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE, blank=True, null=True, related_name='videos')
    _actors = models.ManyToManyField(Actor, related_name='actor_videos', blank=True)
    director = models.ForeignKey(
        Director, 
        on_delete=models.CASCADE, 
        related_name='video_directed', 
        blank=True
    )
    desktop_thumbnail = models.ImageField(
        blank=False,
        null=False,
        upload_to='thumbnail/'
    )
    mobile_thumbnail = models.ImageField(
        blank=False,
        null=False,
        upload_to='thumbnail/'
    )
    mobile_banner = models.ImageField(
        blank=False,
        null=False,
        upload_to='banner/'
    )
    desktop_banner = models.ImageField(
        blank=False,
        null=False,
        upload_to='banner/'
    )
    _genres = models.ManyToManyField(Genre, related_name='genres_videos', blank=True)
    _moods = models.ManyToManyField(Mood, related_name='videos', blank=True)
    video_link = models.URLField(max_length=300, blank=False, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='videos_uploaded')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    video_like = models.ManyToManyField(User, related_name='likes', blank=True)
    favourites = models.ManyToManyField(Profile, related_name='favourites', blank=True)
    published = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Videos"
        verbose_name = "Video"
    
    @property
    def actors(self):
        actors = self._actors.all()
        result = [{
            "id": actor.id,
            "name": actor.name,
            "bio": actor.bio,
            "image": actor.image.url
        } for actor in actors]
        return result
    
    @property
    def mood(self):
        moods = self._moods.all()
        result = [mood.name for mood in moods]
        return result

    @property
    def genres(self):
        genres = self._genres.all()
        result = [genre.name for genre in genres]
        return result
        
    @property
    def rating(self):
        return str(self.age_rating) + "+"
    
    @property
    def likes(self):
        users = self.video_like.all()
        return users.count()

    @property
    def _category(self):
        category = {
            'id': self.category.id,
            'name': self.category.name
        }
        
        return category

    def __str__(self):
        return self.author.user.email


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
