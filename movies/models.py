from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Categories(MPTTModel):
    title = models.CharField(max_length=256)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            db_index=True, on_delete=models.CASCADE, verbose_name='parent сategory')

    class Meta(object):
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return "{}".format(self.title)


class Movies(CommonInfo):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='movies/photos', blank=True, default='groups/photos/joker.png')
    description = models.TextField(blank=True, default='')
    source = models.CharField(max_length=256, blank=True, default='')
    category = models.ManyToManyField(Categories, blank=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    class Meta(CommonInfo.Meta):
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return "{}".format(self.title)

    @property
    def total_likes(self):
        return self.likes.count()


class Actors(CommonInfo):
    name = models.CharField(max_length=256)

    class Meta(CommonInfo.Meta):
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return "{}".format(self.name)


class Actresses(CommonInfo):
    name = models.CharField(max_length=256)

    class Meta(CommonInfo.Meta):
        verbose_name = "Actress"
        verbose_name_plural = "Actresses"

    def __str__(self):
        return "{}".format(self.name)


class Directors(CommonInfo):
    name = models.CharField(max_length=256)

    class Meta(CommonInfo.Meta):
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return "{}".format(self.name)


class Reviews(CommonInfo):
    review = models.TextField()
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta(CommonInfo.Meta):
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return "{}-{}".format(self.user, self.created)
