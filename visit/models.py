from django.db import models
from accounts.models import User


class UserAgent(models.Model):
    is_mobile = models.BooleanField("is mobile")
    is_touch = models.BooleanField("is touch")
    is_tablet = models.BooleanField("is tablet")
    is_pc = models.BooleanField("is pc")
    is_bot = models.BooleanField("is bot")

    browser_family = models.CharField("browser family", max_length=20)
    browser_version = models.CharField("browser version", max_length=10)

    os_family = models.CharField("os family", max_length=20)
    os_version = models.CharField("os version", max_length=10)

    device_family = models.CharField("device family", max_length=20)

class Visitor(models.Model):
    datetime = models.DateTimeField("time of visiting", auto_now=False, auto_now_add=True)
    address = models.CharField("remote address", max_length=20, null=True)
    user_agent = models.OneToOneField("UserAgent", verbose_name="user agent", on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", verbose_name="", on_delete=models.DO_NOTHING, null=True)
