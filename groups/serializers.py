from rest_framework import serializers
from .models import Groups
from authentication.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = '__all__'
