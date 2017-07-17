from django.shortcuts import render

# Create your views here.
def outros(request):
    return render(request, 'outros.html', {'title':'Outros'})

def realizados(request):
    return render(request, 'realizados.html', {'title':'Pedidos realizados'})