from rest_framework import serializers
from .models import Movies, Categories


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'title', 'description', 'source', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title')
