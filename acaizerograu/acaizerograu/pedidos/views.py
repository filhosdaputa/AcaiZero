from django.shortcuts import render
from outros.models import adicional

# Create your views here.
def pedidos(request):
    return render(request, 'pedidos.html', {'title':'Pedidos'})

def acai(request):
    adicionais = adicional.objects.all()
    return render(request, 'acai.html', {'title':'Acai', 'adicionais':adicionais})

def sorvete(request):
    return render(request, 'sorvete.html', {'title':'Sorvete'})