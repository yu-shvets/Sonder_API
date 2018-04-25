from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Posts(CommonInfo):
    picture = models.ImageField(upload_to='posts/pictures', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    class Meta(CommonInfo.Meta):
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return "{}-{}".format(self.user, self.created)

    @property
    def total_likes(self):
        return self.likes.count()


class Comments(MPTTModel, CommonInfo):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='replies', db_index=True)

    class Meta(CommonInfo.Meta):
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return "{}-{}".format(self.user, self.created)

    @property
    def total_likes(self):
        return self.likes.count()


class Messages(CommonInfo):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    message = models.TextField()
    read_status = models.BooleanField(default=False)

    class Meta(CommonInfo.Meta):
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return "{}-{}-{}".format(self.from_user, self.to_user, self.created)
