from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'editor.html')


def landing(request):
    return render(request, 'index.html')
