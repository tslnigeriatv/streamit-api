from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    user_list, 
    user_detail, 
    profile_detail, 
    profile_list, 
    top_trending, 
    # video_category_detail, 
    # video_category_list, 
    # video_detail, 
    # video_list,
    like_video,
    favourite_video,
    
    ActorViewSet,
    GenreViewSet,
    MoodViewSet,
    DirectorViewSet,
    PlayListViewSet,
    VideoCategoryViewSet,
    VideoViewSet,
    
    redirect_socials
)

router = DefaultRouter()
router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'playlists', PlayListViewSet, basename='playlist')
router.register(r'moods', MoodViewSet, basename='mood')
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'categories', VideoCategoryViewSet, basename='category')

urlpatterns = [
    path('user/', user_list, name='user_list'),
    path('user/<int:pk>/', user_detail, name='user_detail'),

    path('profiles/', profile_list, name='profile_list'),
    path('profiles/<int:pk>/', profile_detail, name='profile_detail'),
    # path('video/', video_list, name='video_list'),
    # path('video/<int:pk>/', video_detail, name='video_detail'),

    # Likes
    path('videos/<int:pk>/likes/', like_video, name='like_video'),
    path('videos/<int:pk>/favourites/', favourite_video, name='favourite_video'),
    
    path('videos/trending/', top_trending, name='top_trending'),

    # path('video/category/', video_category_list, name='video_category_list'),
    # path('video/category/<int:pk>/', video_category_detail, name='video_category_detail'),
    
    path('profile/', redirect_socials, name="social"),
    
    path('temporary-redirect-for-testing/', redirect_socials, name="social"),
    
]
urlpatterns += router.urls
