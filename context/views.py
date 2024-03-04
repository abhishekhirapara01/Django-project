from django.shortcuts import render

def hello_view(request):
    context = {'message': 'Hello, Django Context!'}
    return render(request, 'hello_template.html', context)
