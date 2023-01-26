from django.core.paginator import Paginator
# import fertilizer_prediction2
from django.shortcuts import redirect, render
from buysell.models import Form
import requests
import joblib

def gethome(request):
    return render(request, 'index.html')


def post(request):
    name = request.POST.get('name')
    phone_no = request.POST.get('phone_no')
    city = request.POST.get('city')
    state = request.POST.get('state')
    crop_name = request.POST.get('crop_name')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    temp = Form(name=name, phone_no=phone_no, city=city,
                state=state, crop_name=crop_name, quantity=quantity, price=price)
    temp.save()
    # time.sleep(5)
    return redirect('home')

def getlist(request):
    return render(request, 'list.html')