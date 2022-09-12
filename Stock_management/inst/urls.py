from django.urls import path
from . import views

urlpatterns = [
    path('institute/' , views.institute_trade)
]