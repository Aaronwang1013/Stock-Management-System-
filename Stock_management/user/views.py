import http
from django.shortcuts import HttpResponse
from http.client import HTTPResponse
from django.shortcuts import render
from .models import User

# Create your views here.
def reg_view(request):
    #註冊
    #GET 返回頁面

    if request.method == 'GET':
        return render(request , 'user/register.html')
    #POST 處理提交數據
    # 1. 輸入兩次密碼，且須保持一致
    # 2. 當前用戶名是否可用
    # 3. 插入數據 [明文處理密碼]
    elif request.method =='POST':
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']

        if password1 != password2 :
            return HttpResponse('兩次密碼不一致')
        
        old_users = User.objects.filter(username = username)
        if old_users:
            return HttpResponse('該用戶名已使用過')
        User.objects.create(username= username , password = password1)
        return HttpResponse('註冊成功')

        