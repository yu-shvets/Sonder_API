from django.shortcuts import render
from rest_framework import generics
from .models import Movies, Categories
from .serializers import MovieSerializer, CategorySerializer
from rest_framework.filters import SearchFilter


class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title',)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
