from django.db import models
from django.contrib.auth.models import User
from movies.models import Movies, Actors, Actresses, Directors
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class UserProfiles(CommonInfo):

    user = models.OneToOneField(User, related_name='profile')
    photo = models.ImageField(upload_to='users/photos')
    birthdate = models.DateField()
    bio = models.TextField()
    top_movies = models.ManyToManyField(Movies, blank=True)
    top_actors = models.ManyToManyField(Actors, blank=True)
    top_actresses = models.ManyToManyField(Actresses, blank=True)
    top_directors = models.ManyToManyField(Directors, blank=True)

    class Meta(CommonInfo.Meta):
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return "{}".format(self.user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
