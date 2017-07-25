from django.shortcuts import render
from caixa.models import caixa
from decimal import Decimal

# Create your views here.
def caixa1(request):
    total = caixa.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'total':total})

def retirada(request):
    total = caixa.objects.latest('id')
    return render(request, 'retirada.html', {'title':'Retirada', 'total':total})

def retirada_1(request):
    
    retirada1 = request.GET.get('retirada')
    caixatotal1 = caixa.objects.latest('id')
    retirada1 = Decimal(retirada1)
    caixatotal1.total = (caixatotal1.total-retirada1)
    caixatotal2 = caixa(total=caixatotal1.total , tipo="Saida")
    caixatotal2.save()
    total = caixatotal2.total
    retirada2 = retirada1
    return render(request, 'retirada_1.html', {'title':'Retirada', 'total':total, 'retirada1':retirada2})

def fechar(request):
    total = caixa.objects.latest('id')
    return render(request, 'fechar.html', {'title':'Fechar', 'total':total})

def fechar_1(request):
    
    retirada1 = request.GET.get('retirada')
    caixatotal1 = caixa.objects.latest('id')
    retirada1 = Decimal(retirada1)
    caixatotal1.total = (caixatotal1.total-retirada1)
    caixatotal2 = caixa(total=caixatotal1.total , tipo="Saida")
    caixatotal2.save()
    total = caixatotal2.total
    retirada2 = retirada1
    return render(request, 'fechar_1.html', {'title':'Retirada', 'total':total, 'retirada1':retirada2})