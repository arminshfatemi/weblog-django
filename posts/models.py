from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=400, default="no text :(")
    hidden = models.BooleanField(default=False)


    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    decription = models.CharField(max_length=95, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'
