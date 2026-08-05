from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    create_at = models.DateField()

