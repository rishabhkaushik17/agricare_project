from django.core.paginator import Paginator
# import fertilizer_prediction2
from django.shortcuts import redirect, render
from buysell.models import Form
import requests
import joblib

def gethome(request):
    return render(request, 'index.html')