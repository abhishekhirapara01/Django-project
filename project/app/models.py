from django.db import models

# Create your models here.
class Students(models.Model):
  Name =  models.CharField(max_length=100)
  Subjects = models.CharField(max_length=100)
  def  __str__(self): 
    return self.Name
