from django.shortcuts import render
from caixa.models import caixa

# Create your views here.
def caixa1(request):
    total = caixa.objects.latest('id')
    return render(request, 'caixa.html', {'title':'Caixa', 'total':total})