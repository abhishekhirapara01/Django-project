from django.db import models
#from django.db.models import Model


# Create your models here.
class learnmodel(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField(default=0)
  email = models.EmailField(blank=True, null=True)
  folder_upload = models.FileField()
  
  def __str__(self):
    return self.firstname 