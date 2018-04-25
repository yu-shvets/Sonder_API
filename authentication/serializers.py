from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfiles
from friendship.models import Friend, FriendshipRequest


class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        exclude = ('user',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class FriendsSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()

    class Meta:
        model = Friend
        fields = ('from_user',)


class FriendshipRequestsSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()

    class Meta:
        model = FriendshipRequest
        fields = ('from_user',)
