"""StockManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
import re
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/2003/' , views.page_2003_view),
    path('' , views.index_view),
    path('page/1' , views.page1_view),
    path('page/2' , views.page2_view),
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',views.birthday_view),
    #http://127.0.0.1:8000/整數/字串/整數
    path('<int:n>/<str:op>/<int:m>' , views.cal_view),
    path('test_html' , views.test_html),
    path('test_html_params' , views.test_html_params),
    path('test_it_for' , views.test_if_for),
    path('mycal' , views.test_mycal),
    path('base_index' , views.base_view),
    path('music_index' , views.music_view),
    path('sport_index' , views.sport_view),
    path('test_static' , views.test_static)

]

