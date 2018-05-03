from rest_framework import serializers
from .models import Groups
from authentication.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    author = UserSerializer()

    class Meta:
        model = Groups
        fields = '__all__'


class GroupCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        exclude = ('author',)

