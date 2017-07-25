from django.shortcuts import render
from outros.models import adicional, acai, acaimix, casadinho, acaicreme, acaienergy, produto, milkshake, petit, fondue, sorvete
from .models import comanda, comanda_acai, comanda_acaimix, comanda_casadinho, comanda_acaicreme, comanda_acaienergy, comanda_milkshake, comanda_petit, comanda_fondue, comanda_sorvete
from caixa.models import caixa
from decimal import Decimal

# Create your views here.
def pedidos(request):
    return render(request, 'pedidos.html', {'title':'Pedidos'})

def acai1(request):
    return render(request, 'acai.html', {'title':'Acai'})
    
def acai_1(request):
    adicionais = adicional.objects.all()
    acai_tipo = request.GET.get('acai2')
    return render(request, 'acai_1.html', {'title':'Tamanho e Adicionais', 'adicionais':adicionais, 'acai_tipo':acai_tipo})

def sorvete1(request):
    return render(request, 'sorvete.html', {'title':'Sorvete'})

def sorvete_1(request):
    adicionais = adicional.objects.all()
    sorvete1 = request.GET.get('sorvete')
    return render(request, 'sorvete_1.html', {'title':'Sorvete', 'sorvete1':sorvete1, 'adicionais':adicionais})

def finalizar(request):
    acai1 = request.GET.get('acai')
    acaimix1 = request.GET.get('acaimix')
    casadinho1 = request.GET.get('casadinho')
    creme1 = request.GET.get('creme')
    acaienergy1 = request.GET.get('acaienergy')
    milkshake1 = request.GET.get('milkshake')
    
    if acai1 != None and acaimix1 == None and casadinho1 == None and creme1 == None and acaienergy1 == None and milkshake1 == None:
        if acai1 != "acaipuro":
            acai3 = "acaidiverso"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho1, 'adicionais1':adicionais1})
        else:
            acai3 = acai1
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
              
            return render(request, 'finalizar.html', {'title':'Finalizar', 'acai3':acai3, 'tamanho':tamanho1, 'adicionais1':adicionais1})
        
    elif acai1 == None and acaimix1 != None and casadinho1 == None and creme1 == None and acaienergy1 == None and milkshake1 == None:
        acaimix = "acaimix"
        tamanho = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'acaimix':acaimix, 'tamanho':tamanho, 'adicionais1':adicionais1})
    elif acai1 == None and acaimix1 == None and casadinho1 != None and creme1 == None and acaienergy1 == None and milkshake1 == None:
        casadinho = "casadinho"
        tamanho = request.GET.get('tamanho')
        adicionais1 = request.GET.getlist('adicional')
        
        return render(request, 'finalizar.html', {'title':'Finalizar', 'casadinho':casadinho, 'tamanho':tamanho, 'adicionais1':adicionais1})
    elif acai1 == None and acaimix1 == None and casadinho1 == None and creme1 != None and acaienergy1 == None and milkshake1 == None:
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
    elif acai1 == None and acaimix1 == None and casadinho1 == None and creme1 == None and acaienergy1 != None and milkshake1 == None:
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
    elif acai1 == None and acaimix1 == None and casadinho1 == None and creme1 == None and acaienergy1 == None and milkshake1 != None:
        if milkshake1 == "milkcremebranco" or milkshake1 == "milkmorango" or milkshake1 == "milkchocolate" or milkshake1 == "milkninho" or milkshake1 == "milkovomaltine" or milkshake1 == "milkoreo" or milkshake1 == "milkcappuccino" or milkshake1 == "milkpacoca" or milkshake1 == "cookies":
            milkshake = "milkshake1"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar.html', {'title':'Finalizar', 'milkshake':milkshake, 'tamanho':tamanho1, 'adicionais1':adicionais1})
        else:
            milkshake = "milkshake2"
            tamanho1 = request.GET.get('tamanho')
            adicionais1 = request.GET.getlist('adicional')
              
            return render(request, 'finalizar.html', {'title':'Finalizar', 'milkshake':milkshake, 'tamanho':tamanho1, 'adicionais1':adicionais1})
    
    

def finalizar_1(request):
    fondue1 = request.GET.get('fondue')
    petit1 = request.GET.get('petit')
    sorvete1 = request.GET.get('sorvete')
    if fondue1 != None and petit1 == None and sorvete1 == None:
        if fondue1 == 'zerograu' or fondue1 == 'kids':
            fondue1 = "fondue2"
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar_1.html', {'title':'Finalizar', 'fondue1':fondue1, 'adicionais1':adicionais1})
        else:
            fondue1 = "fondue1"
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar_1.html', {'title':'Finalizar', 'fondue1':fondue1, 'adicionais1':adicionais1})
    elif fondue1 == None and petit1 != None and sorvete1 == None:
        petit = petit1
        adicionais1 = request.GET.getlist('adicional')
              
        return render(request, 'finalizar_1.html', {'title':'Finalizar', 'petit':petit, 'adicionais1':adicionais1})
    elif fondue1 == None and petit1 == None and sorvete1 != None:
        if sorvete1 == 'kids' or sorvete1 == 'morango' or sorvete1 == 'napolitano' or sorvete1 == 'merenguemorango' or sorvete1 == 'brigadeiro' or sorvete1 == 'beijinho' or sorvete1 == 'ninho' or sorvete1 == 'sonhodevalsa' or sorvete1 == 'ourobranco' or sorvete1 == 'lacta' or sorvete1 == 'kitkat' or sorvete1 == 'bis' or sorvete1 == 'ovomaltine' or sorvete1 == 'oreo' or sorvete1 == 'churros':
            sorvete1 = "diverso"
            adicionais1 = request.GET.getlist('adicional')
              
            return render(request, 'finalizar_1.html', {'title':'Finalizar', 'sorvete1':sorvete1, 'adicionais1':adicionais1})
        else:
            adicionais1 = request.GET.getlist('adicional')
            return render(request, 'finalizar_1.html', {'title':'Finalizar', 'sorvete1':sorvete1, 'adicionais1':adicionais1})



def pagamento(request):
    pedido = request.GET.get('pedido')
    tamanho = request.GET.get('tamanho')
    qnt = request.GET.get('qnt')
    if pedido == 'acaipuro' and tamanho == 'P'and qnt == None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'P' and qnt != None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'G' and qnt != None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaipuro' and tamanho == 'G' and qnt == None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'P' and qnt != None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'P' and qnt == None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'G' and qnt != None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaidiverso' and tamanho == 'G' and qnt == None:
        acaiteste = acai.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_acai(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'P' and qnt == None:
        acaiteste = acaimix.objects.filter(tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'P' and qnt != None:
        acaiteste = acaimix.objects.filter(tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'G' and qnt == None:
        acaiteste = acaimix.objects.filter(tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'acaimix' and tamanho == 'G' and qnt != None:
        acaiteste = acaimix.objects.filter(tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaimix(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'casadinho' and tamanho == 'P' and qnt == None:
        acaiteste = casadinho.objects.filter(tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'casadinho' and tamanho == 'P' and qnt != None:
        acaiteste = casadinho.objects.filter(tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'casadinho' and tamanho == 'G' and qnt == None:
        acaiteste = casadinho.objects.filter(tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'casadinho' and tamanho == 'G' and qnt != None:
        acaiteste = casadinho.objects.filter(tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_casadinho(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'P' and qnt == None:
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'P' and qnt != None:
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'G' and qnt == None:
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremepuro' and tamanho == 'G' and qnt != None:
        acaiteste = acaicreme.objects.filter(img=pedido,tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'G' and qnt == None:
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'G' and qnt != None:
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'P' and qnt == None:
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cremediverso' and tamanho == 'P' and qnt != None:
        acaiteste = acaicreme.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaicreme(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'P' and qnt == None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'P' and qnt != None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'G' and qnt == None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bomba' and tamanho == 'G' and qnt != None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'P' and qnt == None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'P' and qnt != None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'G' and qnt == None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'tribomba' and tamanho == 'G' and qnt != None:
        acaiteste = acaienergy.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_acaienergy(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake1' and tamanho == 'P' and qnt == None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake1' and tamanho == 'P' and qnt != None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake1' and tamanho == 'G' and qnt == None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake1' and tamanho == 'G' and qnt != None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake2' and tamanho == 'P' and qnt == None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake2' and tamanho == 'P' and qnt != None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='P').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake2' and tamanho == 'G' and qnt == None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'milkshake2' and tamanho == 'G' and qnt != None:
        acaiteste = milkshake.objects.filter(img=pedido, tamanho='G').get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_milkshake(itens=acaiteste, tamanho=tamanho, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'classico' and tamanho == None and qnt == None:
        acaiteste = petit.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_petit(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'kids' and tamanho == None and qnt == None:
        acaiteste = petit.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_petit(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'classico' and tamanho == None and qnt != None:
        acaiteste = petit.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_petit(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'kids' and tamanho == None and qnt != None:
        acaiteste = petit.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_petit(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'fondue1' and tamanho == None and qnt == None:
        acaiteste = fondue.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_fondue(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'fondue2' and tamanho == None and qnt == None:
        acaiteste = fondue.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_fondue(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'fondue1' and tamanho == None and qnt != None:
        acaiteste = fondue.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_fondue(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'fondue2' and tamanho == None and qnt != None:
        acaiteste = fondue.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_fondue(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('total')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'diverso' and tamanho == None and qnt == None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'diverso' and tamanho == None and qnt != None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cascao' and tamanho == None and qnt == None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'cascao' and tamanho == None and qnt != None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'simples' and tamanho == None and qnt == None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'simples' and tamanho == None and qnt != None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'sundae' and tamanho == None and qnt == None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'sundae' and tamanho == None and qnt != None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bananasplit' and tamanho == None and qnt == None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    elif pedido == 'bananasplit' and tamanho == None and qnt != None:
        acaiteste = sorvete.objects.filter(img=pedido).get()
        total = acaiteste.preco+2*int(qnt)
        controle = comanda_sorvete(itens=acaiteste, total=total)
        controle.save()
        caixatotal1 = caixa.objects.latest('id')
        caixatotal1.total = caixatotal1.total+controle.total
        caixatotal2 = caixa(total=caixatotal1.total)
        caixatotal2.save()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'total':total})
    
    return render(request, 'pagamento.html', {'title':'Pagamento', 'pedido':pedido, 'tamanho':tamanho, 'qnt':qnt})

def pagamento_1(request):
    total1 = request.GET.get('total')
    recebido1 = request.GET.get('recebido')
    if recebido1 != total1:
        total1 = Decimal(total1)
        recebido1 = Decimal(recebido1)
        troco1 = Decimal(recebido1-total1)
        return render(request, 'pagamento_1.html', {'title':'Pagamento', 'total1':total1, 'recebido1':recebido1, 'troco1':troco1})

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

def milkshake1(request):
    return render(request, 'milkshake.html', {'title':'Milk Shake'})

def milkshake_1(request):
    milkshake = request.GET.get('milkshake')
    adicionais = adicional.objects.all()
    return render(request, 'milkshake_1.html', {'title':'Milk Shake', 'milkshake':milkshake, 'adicionais':adicionais})

def petit1(request):
    return render(request, 'petit.html', {'title':'Petit Gateau'})

def petit_1(request):
    petit = request.GET.get('petit')
    adicionais = adicional.objects.all()
    return render(request, 'petit_1.html', {'title':'Petit Gateau', 'petit':petit, 'adicionais':adicionais})

def fondue1(request):
    return render(request, 'fondue.html', {'title':'Fondue'})

def fondue_1(request):
    fondue = request.GET.get('fondue')
    adicionais = adicional.objects.all()
    return render(request, 'fondue_1.html', {'title':'Fondue', 'fondue':fondue, 'adicionais':adicionais})