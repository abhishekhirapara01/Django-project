from django.contrib import admin
from .models import learnmodel

# Register your models here.
class learnmodeladmin(admin.ModelAdmin):
  list_display = ['firstname', 'lastname', 'age', 'email']
  list_filter = ['firstname']
admin.site.register(learnmodel, learnmodeladmin)