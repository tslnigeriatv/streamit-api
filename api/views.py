from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from users.models import CustomUser as User
from api.models import (
    Video, 
    VideoCategory, 
    Profile, 
    Actor, 
    Genre,
    Mood,
    PlayList,
    Director
)
# All serializer classes
from .serializers import (
    UserSerializer, 
    ProfileSerializer, 
    VideoSerializer, 
    VideoCategorySerializer,
    ActorSerializer,
    GenreSerializer,
    MoodSerializer,
    PlayListSerializer,
    DirectorSerializer
)


from rest_framework import viewsets

# Create your views here.

# UserAPIView
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'status_code': 201,
                'detail': 'User was created successfully.', 
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, *args, **kwargs):
    try:
        user = get_object_or_404(User, pk=kwargs['pk'])
    except User.DoesNotExist:
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = request.data
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'DELETE':
        user.delete()
        return Response({'details': f'user {kwargs["pk"]} was successfully deleted'}, status=status.HTTP_204_NO_CONTENT)



# ProfileAPIView
# Here Profile Object should be ReadOnly
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    

@api_view(['PUT', 'DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def profile_detail(request, *args, **kwargs):
    try:
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
    except Profile.DoesNotExist:
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = request.data
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VideoAPIView
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def video_list(request):
#     if request.method == 'GET':
#         videos = Video.objects.all()
#         serializer = VideoSerializer(videos, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         data = request.data
#         serializer = VideoSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        
        

# @api_view(['PUT', 'DELETE', 'GET'])
# @permission_classes([IsAuthenticated])
# def video_detail(request, *args, **kwargs):
#     try:
#         video = get_object_or_404(Video, pk=kwargs['pk'])
#     except Video.DoesNotExist:
#         return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = VideoSerializer(video)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         data = request.data
#         serializer = VideoSerializer(video, data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
#     if request.method == 'DELETE':
#         video.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# # VideoCategoryAPIView
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def video_category_list(request):
#     if request.method == 'GET':
#         videos_cat = VideoCategory.objects.all()
#         serializer = VideoCategorySerializer(videos_cat, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         data = request.data
#         serializer = VideoCategorySerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT', 'DELETE', 'GET'])
# @permission_classes([IsAuthenticated])
# def video_category_detail(request, *args, **kwargs):
#     try:
#         video_cat = get_object_or_404(VideoCategory, pk=kwargs['pk'])
#     except Video.DoesNotExist:
#         return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = VideoCategorySerializer(video_cat)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         data = request.data
#         serializer = VideoCategorySerializer(video_cat, data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error, status=status.HTTP_304_NOT_MODIFIED)
#     if request.method == 'DELETE':
#         video_cat.delete()
#         return Response({"details": "Video was deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


def hasId(model, id):
    # Firstly, iterate through all the ids in the model
    # Secondly, check if id exists in all the list of ids[]
    # Thirdly, return True if id exists, else return False
    ids = [instance.id for instance in model]
    if int(id) in ids:
        return True
    else:
        return False

# Like functionality
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_video(request, *args, **kwargs):

    user_id = request.data.get('user_id', None)
    video_id = kwargs['pk']
    
    if video_id is not None and user_id is not None:
        try:
            video = get_object_or_404(Video, pk=video_id)
            user = get_object_or_404(User, pk=user_id)
            if hasId(video.video_like.all(), user_id):
                video.video_like.remove(user)
                return Response({"detail": f"{user.email} unliked {video.title}"})
            else:
                video.video_like.add(user)
                return Response({"detail": f"{user.email} liked {video.title}"})
        except:
            return Response({"details": "Invalid video_id and user_id"})
    
    return Response({"details": "User Id or Video Id cannot be null"})


# Favourites functionality
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def favourite_video(request, *args, **kwargs):

    profile_id = request.data.get('profile_id', None)
    video_id = kwargs['pk']
    
    if video_id is not None and profile_id is not None:
        try:
            video = get_object_or_404(Video, pk=int(video_id))
            profile = get_object_or_404(Profile, pk=int(profile_id))
            if hasId(video.favourites.all(), profile_id):
                video.favourites.remove(profile)
                return Response({"detail": f"{profile.user.email} removed {video.title} from list"})
            else:
                video.favourites.add(profile)
                return Response({"detail": f"{profile.user.email} added {video.title} to list"})
        except:
            return Response({"details": "Invalid video_id and profile_id"})
    
    return Response({"details": "Profile Id or Video Id cannot be null"})


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    
class VideoCategoryViewSet(viewsets.ModelViewSet):
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    permission_classes = [IsAuthenticated]


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]
    
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
    

class MoodViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
    permission_classes = [IsAuthenticated]
    
class PlayListViewSet(viewsets.ModelViewSet):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    permission_classes = [IsAuthenticated]
    

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]
    
    
@api_view(['GET'])
def home(request):
    return render(request, 'index.html', {})
    
@api_view(['GET', 'POST'])
def activate_account(request, uid, token):
    
    return render(request, 'activate_account.html', {
        "uid": uid,
        "token": token
    })
    
    