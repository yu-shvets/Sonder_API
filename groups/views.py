from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Groups
from .serializers import GroupSerializer, GroupCreateSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User


class GroupsList(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupCreateSerializer


class GroupsCreate(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class GroupsList(viewsets.ViewSet):
#
#     def list(self, request):
#         users = User.objects.filter(pk=request.user.pk)
#         queryset = Groups.objects.filter(members__in=users)
#         serializer = GroupSerializer(queryset, many=True)
#         return Response(serializer.data)