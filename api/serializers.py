from rest_framework import serializers
from users.models import CustomUser as User
from .models import (
    Profile, 
    Video, 
    VideoCategory, 
    PlayList,
    Mood,
    Director,
    Actor,
    Genre
)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ['id', 'title', '_videos']
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', '_videos']

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['id', 'name', '_videos']
        
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'bio', 'image', '_videos']
        
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name','bio', 'image', '_videos']
        


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields =  [
            'id', 
            'title', 
            'mobile_thumbnail', 
            'desktop_thumbnail', 
            'mobile_banner', 
            'desktop_banner', 
            'description',
            'video_link', 
            '_category', 
            'likes', 
            'actors',
            'playlist',
            'rating',
            'mood',
            'genres',
            'published',
            "more_like_this",
            'date_uploaded', 
            'last_modified'
        ]

        
class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'email', 
            'is_superuser', 
            'is_active', 
            'date_joined',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                
            },
            'password2': {
                'write_only': True,
                
            }
        }
        
    def save(self):
        user = User(email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        else:
            user.set_password(password)
            user.save()
            return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user_details', 
            'username', 
            'first_name', 
            'last_name', 
            'profile_photo', 
            'bio', 
            'favourite_videos', 
            'country', 
            'gender', 
            'phone_number'
        ]
        



class VideoCategorySerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = VideoCategory
        fields = ['id', 'name', 'videos'] 
