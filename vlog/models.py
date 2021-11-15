from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from mptt.models import MPTTModel, TreeForeignKey


class TzUser(AbstractUser):
    email = models.EmailField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='media', default='defaultphoto.jpg', blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.username)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='media', default='defaultpost.jpg', blank=True, null=True)
    author = models.ForeignKey(TzUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Comments(MPTTModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(TzUser, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.comment)
