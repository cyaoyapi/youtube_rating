from django.urls import path, include
from rest_framework import routers
from .views import VideoViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
