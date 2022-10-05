from pyexpat import model
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Book (models.Model):
    title=models.CharField(max_length=30,null=True,blank=True)
    excerpt=models.TextField()


    def __str__(self):
        return self.title

