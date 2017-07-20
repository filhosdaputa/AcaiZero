from django.shortcuts import render
from outros.models import adicional, acai
from .models import comanda, comanda_acai
from caixa.models import caixa
# Create your views here.
def pedidos(request):
    return render(request, 'pedidos.html', {'title':'Pedidos'})

def acai1(request):
    adicionais = adicional.objects.all()

    return render(request, 'acai.html', {'title':'Acai', 'adicionais':adicionais})
    

def acai_1(request):
    adicionais = adicional.objects.all()
    acai_tipo = request.GET.get('acai2')
    return render(request, 'acai_1.html', {'title':'Tamanho e Adicionais', 'adicionais':adicionais, 'acai_tipo':acai_tipo})

def sorvete(request):
    return render(request, 'sorvete.html', {'title':'Sorvete'})

def finalizar(request):
    if request.GET.get('acai') == 'acaipuro' and request.GET.get('tamanho') == 'P':
        acai3 = request.GET.get('acai')
        tamanho1 = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        qnt = request.GET.getlist('adicional')
        total = 11
        
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho1, 'adicionais1':adicionais1, 'total':qnt})
    elif request.GET.get('acai') != 'puro':
        acai3 = request.GET.get('acai')
        tamanho = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho, 'adicionais1':adicionais1})

def pagamento(request):
    acai3 = request.GET.get('acai')
    tamanho = request.GET.get('tamanho')
    qnt = request.GET.get('qnt')
    if acai3 == 'acaipuro' and tamanho == 'P'and qnt == None:
        total = 11
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif acai3 == 'acaipuro' and tamanho == 'P' and qnt != None:
        total = 11+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif acai3 == 'acaipuro' and tamanho == 'G' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif acai3 == 'acaipuro' and tamanho == 'G' and qnt == None:
        total = 13
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif acai3 != 'acaipuro' and tamanho == 'P' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif acai3 != 'acaipuro' and tamanho == 'P' and qnt == None:
        total = 13
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif acai3 != 'acaipuro' and tamanho == 'G' and qnt != None:
        total = 15+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif acai3 != 'acaipuro' and tamanho == 'G' and qnt == None:
        total = 15
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    
    return render(request, 'pagamento.html', {'title':'Pagamento', 'acai3':acai3, 'tamanho':tamanho, 'qnt':qnt})