from django.http import HttpResponse
from django.template import loader
from .models import Students
from django.shortcuts import render

def testing(request):
  mydata = Students.objects.all()
  template = loader.get_template('template.html')
  context = {
    'students': mydata,
  }
  return HttpResponse(template.render(context, request))


def view(request):
  students2 = Students.objects.all()
  students = request.GET.get('students')
  return render (request,'template.html',{'students':students, 'students2': students2})

def home(request):
  return render(request, 'home.html')
