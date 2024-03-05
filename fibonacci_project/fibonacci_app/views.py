from django.shortcuts import render
from .utils import timing_decorator,fibonacci_generator
# Create your views here.

@timing_decorator
def fibonacci_view(request, n):
  n = int(n)
  fib_numbers = list(fibonacci_generator(n))
  context = {'n': n, 'fib_numbers': fib_numbers}
  return render(request, 'fibonacci_template.html', context)

def home(request):
    return render(request, 'home.html') 