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


def display(request):
    obj = Form.objects.all()
    return render(request, 'sell.html', locals())

def get_recommendation(request):
    return render(request, 'recommend.html')

def get_crop_result(request):
    cls = joblib.load('final_model.sav')

    lis = []
    lis.append(request.POST.get('n'))
    lis.append(request.POST.get('p'))
    lis.append(request.POST.get('k'))
    lis.append(request.POST.get('temp'))
    lis.append(request.POST.get('hum'))
    lis.append(request.POST.get('ph'))
    lis.append(request.POST.get('rain'))

    ans = cls.predict([lis])
    s = ""
    s = s.join(ans)
    return render(request, 'crop_result.html', {'ans': s})
