from django.db import models


class Visitor(models.Model):
    datetime = models.DateTimeField("time of visiting", auto_now=False, auto_now_add=True)
    user_agent = models.TextField("info about vititor")
    address = models.CharField("remote address", max_length=20, null=True)