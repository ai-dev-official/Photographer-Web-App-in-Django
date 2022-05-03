from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
from django.core.files import File
from django.utils.text import slugify 
from django.utils import timezone
#from jsonfield import JSONField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    ordering = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/%s/' % (self.slug)


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,  null=True, blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='')
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    visits = models.IntegerField(default=0)
    last_visit = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE,
      
    )
    likes = models.ManyToManyField(
        User, related_name='photo_likes')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Photo, self).save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('photo', args=[str(self.id)])

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)


# class Comment(models.Model):
#     photo = models.ForeignKey(
#         Photo,
#         on_delete=models.CASCADE,
#         related_name='comments'
#     )
#     email = models.CharField(max_length=100)
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
#         default=1
#     )
#     comment = models.TextField(default=False)
#     body = models.TextField(default=False)
#     url = models.TextField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)

#     class meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.author)

#     def get_absolute_url(self):
#         return reverse('photo')
