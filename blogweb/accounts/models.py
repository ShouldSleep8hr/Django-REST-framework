from django.db import models

from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    # class Meta:
    #     permissions = (("can_edit_blog", "can_comment"),)

    def __str__(self):
        return self.username

