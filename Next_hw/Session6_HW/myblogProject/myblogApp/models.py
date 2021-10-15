from django.db import models

# Create your models here.
class Posting(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    writetime = models.CharField(max_length=20)

    def __str__(self):
        return self.title

