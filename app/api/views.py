from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Video, Rating
from .serializers import VideoSerializer, RatingSerializer, UserSerializer

# Create your views here.

class VideoViewSet(viewsets.ModelViewSet):
    """Viewset for videos objects"""

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.AllowAny,)


class RatingViewSet(viewsets.ModelViewSet):
    """Viewset for videos objects"""

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        response = {
            "message": "Rating cannot be updated like this!"
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
