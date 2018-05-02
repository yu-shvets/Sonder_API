from rest_framework import serializers
from .models import Groups
from authentication.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Groups
        fields = '__all__'


class GroupCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        exclude = ('author',)

