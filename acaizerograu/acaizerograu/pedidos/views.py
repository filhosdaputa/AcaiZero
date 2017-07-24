from django.shortcuts import render
from outros.models import adicional, acai, acaimix, casadinho, acaicreme, acaienergy, produto
from .models import comanda, comanda_acai, comanda_acaimix, comanda_casadinho, comanda_acaicreme, comanda_acaienergy
from caixa.models import caixa
# Create your views here.
def pedidos(request):
    return render(request, 'pedidos.html', {'title':'Pedidos'})

def acai1(request):
    return render(request, 'acai.html', {'title':'Acai'})
    
def acai_1(request):
    adicionais = adicional.objects.all()
    acai_tipo = request.GET.get('acai2')
    return render(request, 'acai_1.html', {'title':'Tamanho e Adicionais', 'adicionais':adicionais, 'acai_tipo':acai_tipo})

def sorvete(request):
    return render(request, 'sorvete.html', {'title':'Sorvete'})

def finalizar(request):
    if request.GET.get('acai') != None and request.GET.get('acaimix') == None and request.GET.get('casadinho') == None and request.GET.get('creme') == None and request.GET.get('acaienergy') == None:
        if request.GET.get('acai') != "acaipuro":
            acai3 = "acaidiverso"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho1, 'adicionais1':adicionais1})
        else:
            acai3 = request.GET.get('acai')
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
              
            return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho1, 'adicionais1':adicionais1})
        
    elif request.GET.get('acai') == None and request.GET.get('acaimix') != None and request.GET.get('casadinho') == None and request.GET.get('creme') == None and request.GET.get('acaienergy') == None:
        acaimix = "acaimix"
        tamanho = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'acaimix':acaimix, 'tamanho':tamanho, 'adicionais1':adicionais1})
    elif request.GET.get('acai') == None and request.GET.get('acaimix') == None and request.GET.get('casadinho') != None and request.GET.get('creme') == None and request.GET.get('acaienergy') == None:
        casadinho = "casadinho"
        tamanho = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'casadinho':casadinho, 'tamanho':tamanho, 'adicionais1':adicionais1})
    elif request.GET.get('acai') == None and request.GET.get('acaimix') == None and request.GET.get('casadinho') == None and request.GET.get('creme') != None and request.GET.get('acaienergy') == None:
        if request.GET.get('creme') != "cremepuro":
            creme = "cremediverso"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar.html', {'title':'Finalizar', 'creme':creme, 'tamanho':tamanho1, 'adicionais1':adicionais1})
        else:
            creme = "cremepuro"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
              
            return render(request, 'finalizar.html', {'title':'Finalizar', 'creme':creme, 'tamanho':tamanho1, 'adicionais1':adicionais1})
    elif request.GET.get('acai') == None and request.GET.get('acaimix') == None and request.GET.get('casadinho') == None and request.GET.get('creme') == None and request.GET.get('acaienergy') != None:
        if request.GET.get('acaienergy') == "bomba":
            acaienergy = "bomba"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar.html', {'title':'Finalizar', 'acaienergy':acaienergy, 'tamanho':tamanho1, 'adicionais1':adicionais1})
        else:
            acaienergy = "tribomba"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
              
            return render(request, 'finalizar.html', {'title':'Finalizar', 'acaienergy':acaienergy, 'tamanho':tamanho1, 'adicionais1':adicionais1})
def pagamento(request):
    pedido = request.GET.get('pedido')
    tamanho = request.GET.get('tamanho')
    qnt = request.GET.get('qnt')
    if pedido == 'acaipuro' and tamanho == 'P'and qnt == None:
        total = 11
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'P' and qnt != None:
        total = 11+2*int(qnt)
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'G' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'G' and qnt == None:
        total = 13
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'P' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'P' and qnt == None:
        total = 13
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'G' and qnt != None:
        total = 15+2*int(qnt)
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'G' and qnt == None:
        total = 15
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
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
    elif pedido == 'casadinho' and tamanho == 'P' and qnt == None:
        total = 14
        acaiteste = casadinho.objects.filter(tamanho='P').get()
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'casadinho' and tamanho == 'P' and qnt != None:
        total = 14+2*int(qnt)
        acaiteste = casadinho.objects.filter(tamanho='P').get()
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'casadinho' and tamanho == 'G' and qnt == None:
        total = 16
        acaiteste = casadinho.objects.filter(tamanho='G').get()
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'casadinho' and tamanho == 'G' and qnt != None:
        total = 16+2*int(qnt)
        acaiteste = casadinho.objects.filter(tamanho='G').get()
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'P' and qnt == None:
        total = 11
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'P' and qnt != None:
        total = 11+2*int(qnt)
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'G' and qnt == None:
        total = 12
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'G' and qnt != None:
        total = 12+2*int(qnt)
        acaiteste = acaicreme.objects.filter(img=pedido,tamanho='G').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'G' and qnt == None:
        total = 13
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'G' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'P' and qnt == None:
        total = 12
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'P' and qnt != None:
        total = 12+2*int(qnt)
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'P' and qnt == None:
        total = 11
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'P' and qnt != None:
        total = 11+2*int(qnt)
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'G' and qnt == None:
        total = 12
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'G' and qnt != None:
        total = 12+2*int(qnt)
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'P' and qnt == None:
        total = 12
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'P' and qnt != None:
        total = 12+2*int(qnt)
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'G' and qnt == None:
        total = 13
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'G' and qnt != None:
        total = 13+2*int(qnt)
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    
    return render(request, 'pagamento.html', {'title':'Pagamento', 'pedido':pedido, 'tamanho':tamanho, 'qnt':qnt})

def acaimix1(request):
    return render(request, 'acaimix.html', {'title':'Açaí Mix'})

def acaimix_1(request):
    adicionais = adicional.objects.all()
    acaimix1 = request.GET.get('acaimix')
    return render(request, 'acaimix_1.html', {'title':'Açaí Mix', 'acaimix1':acaimix1, 'adicionais':adicionais})

def casadinho1(request):
    return render(request, 'casadinho.html', {'title':'Açaí Casadinho'})

def casadinho_1(request):
    adicionais = adicional.objects.all()
    casadinho1 = request.GET.get('casadinho')
    return render(request, 'casadinho_1.html', {'title':'Açaí Casadinho', 'casadinho1':casadinho1, 'adicionais':adicionais})

def acaienergy1(request):
    return render(request, 'acaienergy.html', {'title':'Açaí Energy'})

def acaienergy_1(request):
    adicionais = adicional.objects.all()
    acaienergy = request.GET.get('acaienergy')
    return render(request, 'acaienergy_1.html', {'title':'Açaí Energy', 'acaienergy':acaienergy, 'adicionais':adicionais})
    

def acaicreme1(request):
    return render(request, 'acaicreme.html', {'title':'Açaí Creme'})

def acaicreme_1(request):
    adicionais = adicional.objects.all()
    acaicreme = request.GET.get('creme')
    return render(request, 'acaicreme_1.html', {'title':'Açaí Creme', 'acaicreme':acaicreme, 'adicionais':adicionais})

def produtos(request):
    return render(request, 'produtos.html', {'title':'Produtos'})

def produtos_1(request):
    produto1 = request.GET.get('produto')
    if produto1 == 'cocacola':
        acaiteste = produto.objects.filter(img=produto1).get()
        total = acaiteste.preco
        controle = comanda(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif produto1 == 'cocazero':
        acaiteste = produto.objects.filter(img=produto1).get()
        total = acaiteste.preco
        controle = comanda(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif produto1 == 'guarana':
        acaiteste = produto.objects.filter(img=produto1).get()
        total = acaiteste.preco
        controle = comanda(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif produto1 == 'aguacgas':
        acaiteste = produto.objects.filter(img=produto1).get()
        total = acaiteste.preco
        controle = comanda(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif produto1 == 'aguasgas':
        acaiteste = produto.objects.filter(img=produto1).get()
        total = acaiteste.preco
        controle = comanda(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal1.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    return render(request, 'produtos_1.html', {'title':'Produtos'})