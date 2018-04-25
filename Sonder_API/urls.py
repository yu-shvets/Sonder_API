"""Sonder_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken import views
from authentication.views import UserViewSet, CustomAuthToken, FacebookLogin, TwitterLogin, FriendsList, send_request, \
    accept_request, FriendshipRequestsList, cancel_request, remove_friend, UserProfileCreate
from movies.views import MoviesList, MovieDetail
from groups.views import GroupsList, GroupDetail, GroupsCreate
from feeds.views import PostsList, PostDetail

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', CustomAuthToken.as_view()),

    url(r'^api/friends/$', FriendsList.as_view({'get': 'list'})),
    url(r'^api/friendship_requests/$', FriendshipRequestsList.as_view({'get': 'list'})),

    url(r'^api/movies/$', MoviesList.as_view()),
    url(r'^api/movies/(?P<pk>[0-9]+)/$', MovieDetail.as_view()),

    url(r'^api/groups/$', GroupsList.as_view({'get': 'list'})),
    url(r'^api/groups/(?P<pk>[0-9]+)/$', GroupDetail.as_view()),
    url(r'^api/groups/create/$', GroupsCreate.as_view()),

    url(r'^api/posts/$', PostsList.as_view()),
    url(r'^api/posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),

    url(r'^api/user_profile/create/$', UserProfileCreate.as_view()),

    url(r'^send_request/(?P<user_id>\d+)/$', send_request, name='send_request'),
    url(r'^accept_request/(?P<user_id>\d+)/$', accept_request, name='accept_request'),
    url(r'^cancel_request/(?P<user_id>\d+)/$', cancel_request, name='cancel_request'),
    url(r'^remove_friend/(?P<user_id>\d+)/$', remove_friend, name='remove_friend'),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
