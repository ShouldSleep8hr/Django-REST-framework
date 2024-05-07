from django.db import models

from accounts.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)
    created_on = models.DateTimeField("date created", auto_now_add=True)
    updated_on = models.DateTimeField("date updated", auto_now=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title_text = models.CharField(max_length=20)
    content_text = models.CharField(max_length=200)
    created_on = models.DateTimeField("date created", auto_now_add=True)
    updated_on = models.DateTimeField("date updated", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title_text

class Comment(models.Model):
    text = models.CharField(max_length=200)
    created_on = models.DateTimeField("date created", auto_now_add=True)
    updated_on = models.DateTimeField("date updated", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

