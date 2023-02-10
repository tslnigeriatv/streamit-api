from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    user_list, 
    user_detail, 
    profile_detail, 
    profile_list, 
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
    VideoViewSet
)

router = DefaultRouter()
router.register(r'actor', ActorViewSet, basename='actor')
router.register(r'playlist', PlayListViewSet, basename='playlist')
router.register(r'mood', MoodViewSet, basename='mood')
router.register(r'director', DirectorViewSet, basename='director')
router.register(r'genre', GenreViewSet, basename='genre')
router.register(r'video', VideoViewSet, basename='video')
router.register(r'category', VideoCategoryViewSet, basename='category')

urlpatterns = [
    path('user/', user_list, name='user_list'),
    path('user/<int:pk>/', user_detail, name='user_detail'),

    path('profile/', profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile_detail, name='profile_detail'),
    # path('video/', video_list, name='video_list'),
    # path('video/<int:pk>/', video_detail, name='video_detail'),

    # Likes
    path('video/<int:pk>/likes/', like_video, name='like_video'),
    path('video/<int:pk>/favourites/', favourite_video, name='favourite_video'),

    # path('video/category/', video_category_list, name='video_category_list'),
    # path('video/category/<int:pk>/', video_category_detail, name='video_category_detail'),
]
urlpatterns += router.urls
