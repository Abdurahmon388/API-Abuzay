from rest_framework import serializers
from .models import Movie, Actor


class MovieSerializer(serializers.ModelSerializer):
    actor = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = '__all__'
