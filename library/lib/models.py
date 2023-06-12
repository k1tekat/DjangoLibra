from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    namebook = models.CharField(max_length=20)
    takebook = models.ForeignKey(User,on_delete=models.CASCADE())


    def __str__(self):
        return "namebook: {}".format(self.namebook)
