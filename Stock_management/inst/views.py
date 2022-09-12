from django.shortcuts import render
from django.http import HttpResponse
from .models import Institute
# Create your views here.

def index_view(request):
    # return HttpResponse('This is the record of three institute')
    return render(request , 'index.html')

def institute_trade(request):
    institute_trade = Institute.objects.all()
    return render(request , 'institute/institute_trade.html' , locals())