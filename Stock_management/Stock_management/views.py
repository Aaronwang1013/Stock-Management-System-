from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
    # return HttpResponse('This is home page')
    return render(request , 'home.html')

def set_session(request):
    request.session['uname'] = 'wwc'
    return HttpResponse('set session is ok')

def get_session(request):
    value = request.session['uname']
    return HttpResponse('session value is %s'%(value))