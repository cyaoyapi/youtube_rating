from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Video, Rating

class VideoSerializer(serializers.ModelSerializer):
    """Model serializer for model Video"""

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'url', 'category', 'subcategory', 
        'author', 'ratings_average', 'comments_list',)
        extra_kwargs = {
            'url': {
                'required': True,
            }
        }

class RatingSerializer(serializers.ModelSerializer):
    """Model serializer for model Rating"""

    class Meta:
        model = Rating
        fields = ('id', 'video', 'user', 'stars', 'comments',)

class UserSerializer(serializers.ModelSerializer):
    """Model serializer for model User"""

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {
                'required': True,
                'write_only': True
            }
        }

    def create(self, validated_data):
        """Override default create method

        For each user, create and link a token to it.
        This token will be required to use the api.
        """
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user