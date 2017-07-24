
from django.shortcuts import render
from escpos.printer import Usb
import usb

# Create your views here.
def home(request):

    return render(request, 'home/home.html', {'title':'Home'})
