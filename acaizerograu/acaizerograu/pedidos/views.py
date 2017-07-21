from django.shortcuts import render
from outros.models import adicional, acai, acaimix
from .models import comanda, comanda_acai, comanda_acaimix
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
    if acai_tipo == "acaipuro":
        return render(request, 'acai_1.html', {'title':'Tamanho e Adicionais', 'adicionais':adicionais, 'acai_tipo':acai_tipo})
    if acai_tipo != "acaipuro":
        acaimix3 = acaimix3
        return render(request, 'acai_1.html', {'title':'Tamanho e Adicionais', 'adicionais':adicionais, 'acai_tipo':acai_tipo, 'acaimix3':acaimix3})
    return render(request, 'acai_1.html', {'title':'Tamanho e Adicionais', 'adicionais':adicionais, 'acai_tipo':acai_tipo})

def sorvete(request):
    return render(request, 'sorvete.html', {'title':'Sorvete'})

def finalizar(request):
    if request.GET.get('acai') == 'acaipuro' and request.GET.get('tamanho') == 'P' and request.GET.get('acaimix') == None:
        acai3 = request.GET.get('acai')
        tamanho1 = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        qnt = request.GET.getlist('adicional')
        total = 11
        
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho1, 'adicionais1':adicionais1, 'total':qnt})
    elif request.GET.get('acai') != 'puro' and request.GET.get('acaimix') == None:
        acai3 = request.GET.get('acai')
        tamanho = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho, 'adicionais1':adicionais1})
    elif request.GET.get('acai') == None and request.GET.get('acaimix') != None:
        acaimix = request.GET.get('acaimix')
        tamanho = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'acaimix':acaimix, 'tamanho':tamanho, 'adicionais1':adicionais1})

def pagamento(request):
    pedido = request.GET.get('pedido')
    tamanho = request.GET.get('tamanho')
    qnt = request.GET.get('qnt')
    if pedido == 'acaipuro' and tamanho == 'P'and qnt == None:
        total = 11
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'P' and qnt != None:
        total = 11+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'G' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'G' and qnt == None:
        total = 13
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'P' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'P' and qnt == None:
        total = 13
        acaiteste = acai.objects.filter(img=acai3, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'G' and qnt != None:
        total = 15+2*int(qnt)
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'G' and qnt == None:
        total = 15
        acaiteste = acai.objects.filter(img=acai3, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'P' and qnt == None:
        total = 10
        acaiteste = acaimix.objects.filter(tamanho='P').get()
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'P' and qnt != None:
        total = 10+2*int(qnt)
        acaiteste = acaimix.objects.filter(tamanho='P').get()
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'G' and qnt == None:
        total = 12
        acaiteste = acaimix.objects.filter(tamanho='G').get()
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'G' and qnt != None:
        total = 12+2*int(qnt)
        acaiteste = acaimix.objects.filter(tamanho='G').get()
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    
    return render(request, 'pagamento.html', {'title':'Pagamento', 'acai3':acai3, 'tamanho':tamanho, 'qnt':qnt})

def acaimix1(request):
    return render(request, 'acaimix.html', {'title':'Açaí Mix'})

def acaimix_1(request):
    adicionais = adicional.objects.all()
    acaimix1 = request.GET.get('acaimix')
    return render(request, 'acaimix_1.html', {'title':'Açaí Mix', 'acaimix1':acaimix1, 'adicionais':adicionais})