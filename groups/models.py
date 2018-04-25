from django.db import models
from django.contrib.auth.models import User
from movies.models import Movies
from movies.models import Categories


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Groups(CommonInfo):
    name = models.CharField(max_length=256, blank=True, default='')
    image = models.ImageField(upload_to='groups/photos')
    author = models.ForeignKey(User, related_name='author')
    categories = models.ManyToManyField(Categories, blank=True)
    movies = models.ManyToManyField(Movies, blank=True)
    members = models.ManyToManyField(User, blank=True, related_name='group_members')

    class Meta(CommonInfo.Meta):
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return "{}".format(self.name)