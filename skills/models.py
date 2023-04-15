from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#User table already exists in django

class Skills(models.Model):
    skillname = models.CharField(max_length=100,blank = False, null = False)
    
    def __str__(self):
        return str(self.Skills)

class Experience(models.Model):
    title = models.CharField(max_length=100,blank = False, null = False)
    role = models.CharField(max_length=100,blank = False, null = False)
    role =models.CharField(max_length=100, blank = False, null = False)
    start_date = models.DateTimeField(blank=False,null=False)
    end_date = models.DateTimeField(blank=False,null=False)

    def __str__(self):
        return str(self.Experience)

