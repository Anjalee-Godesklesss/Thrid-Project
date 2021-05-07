from django.db import models
from datetime import datetime


class Blog(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images")
    description=models.TextField(max_length=200)
    author=models.CharField(max_length=20)
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

