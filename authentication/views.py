from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from .serializers import UserSerializer, FriendsSerializer, FriendshipRequestsSerializer, UserProfilesSerializer
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer
from friendship.models import Friend, FriendshipRequest
from rest_framework import generics
from .models import UserProfiles
from rest_framework.filters import SearchFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('username',)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class FriendsList(viewsets.ViewSet):

    def list(self, request):
        queryset = Friend.objects.filter(to_user=request.user)
        serializer = FriendsSerializer(queryset, many=True)
        return Response(serializer.data)


def send_request(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    Friend.objects.add_friend(request.user, other_user)
    return HttpResponseRedirect(reverse('home'))


def accept_request(request, user_id):
    friend_request = FriendshipRequest.objects.get(from_user=user_id, to_user=request.user)
    friend_request.accept()
    return HttpResponseRedirect(reverse('home'))


def cancel_request(request, user_id):
    friend_request = FriendshipRequest.objects.get(from_user=user_id, to_user=request.user)
    friend_request.cancel()
    return HttpResponseRedirect(reverse('home'))


def remove_friend(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    Friend.objects.remove_friend(request.user, other_user)
    return HttpResponseRedirect(reverse('home'))


class FriendshipRequestsList(viewsets.ViewSet):

    def list(self, request):
        queryset = FriendshipRequest.objects.filter(to_user=request.user)
        serializer = FriendshipRequestsSerializer(queryset, many=True)
        return Response(serializer.data)


class UserProfileCreate(generics.ListCreateAPIView):
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
