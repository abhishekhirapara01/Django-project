from django.shortcuts import render
from django.http import HttpResponse
from .models import learnmodel

# Create your views here.
def index(request):
  m = learnmodel.objects.all().values()
  return HttpResponse("hello world!")