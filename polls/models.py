from django.db import models
import os

# Create your models here.

class Job(models.Model):
    github_job = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.github_job
    
    

