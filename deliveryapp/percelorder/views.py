from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .form import OrderForm

# Create your views here.
# Create your views here.

def home(request):
        context={}
        return render(request,'percelorder/dashboard.html',context)

def order(request):
        form = OrderForm() 
        contex={'form':form}         
        return render(request,'percelorder/order_form.html',contex)

def merchant(request):
        return HttpResponse('hi')
