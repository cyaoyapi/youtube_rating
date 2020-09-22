from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, authentication, response, decorators
from .models import Video, Rating
from .serializers import VideoSerializer, RatingSerializer, UserSerializer

# Create your views here.

class VideoViewSet(viewsets.ModelViewSet):
    """Viewset for videos objects"""

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.AllowAny,)

    @decorators.action(methods=['PUT'], detail=True)
    def rate_video(self, request, pk=None):
        if 'stars' in request.data:
            video = Video.objects.get(id=pk)
            stars = request.data['stars']
            comments = request.data['comments']
            user = request.user
            try:
                rating = Rating.objects.get(video=video.id, user=user.id)
                rating.stars = stars
                rating.comments = comments
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response_to_send = {
                    "message": "Rating has been updated!",
                    "result": serializer.data
                }
                return response.Response(response_to_send, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(video=video, user=user, stars=stars, comments=comments)
                serializer = RatingSerializer(rating, many=False)
                response_to_send = {
                    "message": "Rating created!",
                    "result": serializer.data
                }
                return response.Response(response_to_send, status=status.HTTP_200_OK)
        else:
            response_to_send = {
                "message": "Please enter stars for rating!"
            }
            return response.Response(response_to_send, status=status.HTTP_400_BAD_REQUEST)
    


class RatingViewSet(viewsets.ModelViewSet):
    """Viewset for videos objects"""

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        response_to_send = {
            "message": "Rating cannot be updated like this!"
        }
        return response.Response(response_to_send, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """Viewset for User objects"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

