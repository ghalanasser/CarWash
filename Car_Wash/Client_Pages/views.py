from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Client_Pages/base.html')