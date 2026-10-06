from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    rating = serializers.IntegerField(
        min_value=0,
        max_value=5
    )

    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']

        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['user', 'menuitem_id']
            )
        ]