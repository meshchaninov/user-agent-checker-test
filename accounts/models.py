from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    icon = models.ImageField("image of user", upload_to='photos', default='default/default-user.jpg')

