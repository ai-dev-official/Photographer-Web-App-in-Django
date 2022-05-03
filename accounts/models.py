from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
#from PhotographyWebsite.settings import AUTH_USER_MODEL
from django.contrib.auth.models import User

# Create your models here.


# class CustomUser(AbstractUser):
#     age = models.PositiveBigIntegerField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='static/images/avatar.png', upload_to='static/images/', null=True, blank=True)
    date_of_birth = models.DateField(null=False, blank = False)
    fav_author = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    hobbies = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    website = models.URLField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s' % self.user.username


User.accounts = property(lambda u: Profile.objects.get_or_create(user=u)[0])


#    from django.contrib.auth.models import User
#    from accounts.models import Profile
#    from django.contrib.auth import get_user_model
#    User = get_user_model()
#    users = User.objects.filter(profile=None)
#    for user in users:
#        Profile.objects.create(user=user)
