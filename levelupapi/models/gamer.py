from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    is_master_gamer = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name}'
