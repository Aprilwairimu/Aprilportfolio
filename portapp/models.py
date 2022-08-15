from django.db import models

# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=100, null=True, blank=True)
    