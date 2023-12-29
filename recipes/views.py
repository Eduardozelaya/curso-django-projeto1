from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context= {
         'name': 'Eduardo Zelaya',
    })

def contato(request):
    return render(request, 'me-apague/temp.html')
 
def sobre(request):
    return HttpResponse('SOBRE')