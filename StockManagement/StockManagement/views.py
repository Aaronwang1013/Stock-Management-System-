from django.http import HttpResponse
from django.shortcuts import render

def page_2003_view(request):
    html = '<h1>第一個頁面<h1>'
    return HttpResponse(html)


def index_view(request):
    html = '這是我得的首頁'
    return HttpResponse(html)

def page1_view(request):
    html = '這是編號1的網頁'
    return HttpResponse(html)

def page2_view(request):
    html = '這是編號2的網頁'
    return HttpResponse(html)

def cal_view(request , n , op , m):
    if op not in ['add' , 'sub' , 'mul']:
        return HttpResponse('OP is wrong')
    result = 0

    if op == 'add' :
        result = n+m
    elif op == 'sub' :
        result = n-m
    elif op == 'mul' :
        result = m*n 
    return HttpResponse('result is %s'%(result))

def birthday_view(request , y, m,d):
    html = 'birthday is %syear %smonth %sday'%(y , m , d)
    return HttpResponse(html)

def test_html(request):
    #方案一
    # from django.template import loader 
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    
    #方案二
    # from django.shortcuts import render
    dic = {'username':'aaronwang' , 'age': 18}

    return render(request , 'test_html.html' , dic)


def test_html_params(request):
    # from django.shortcuts import render
    dic = {}
    dic['int'] = 88
    dic['str'] = 'aaronwang'
    dic['lst'] = ['Tom' , 'Jack' , 'Lily']
    dic['dict'] = {'a':9 , 'b':8} 
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    dic['script'] = '<script>alert(1111)</script>'

    return render(request , 'test_html_params.html' , dic)

def say_hi():
    return 'haha'


class Dog:
    def say(self):
        return 'wangwang'


def test_if_for(request):
    # from django.shortcuts import render
    dict = {}
    dict['x'] = 10
    return render(request , 'test_if_for.html' , dict)

def test_mycal(request):

    if request.method == 'GET':
        return render(request , 'mycal.html')

    elif request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        result = 0
        if op =='add':
            result = x+y
        elif op == 'sub':
            result = x-y
        elif op == 'mul':
            result = x*y
        elif op == ' div':
            result = x/y
        # dict = {}
        # dict['x'] = x
        # dict['y'] = y 
        # dict['op'] = op
        # dict['result'] = result
        #locals()功能可以自動建立字典
        return render(request , 'mycal.html' , locals())
    

def base_view(request):
    return render(request , 'base.html')


def music_view(request):
    return render(request , 'music.html')


def sport_view(request):
    return render(request , 'sport.html')

def test_static(request):
    return render(request , 'test_static.html')