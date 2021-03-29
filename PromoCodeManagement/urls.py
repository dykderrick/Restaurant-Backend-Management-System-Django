# -*- coding: utf-8 -*-
# @Time    : 3/29/21 09:59
# @Author  : Yingke Ding
# @FileName: urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'PromoCodeManagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_code/', views.add_code, name='add'),
    path('edit_code/<str:oid>/', views.edit_code, name='edit'),
    path('delete_code/<str:oids>/', views.delete_code, name='delete'),
    path('delete_code/', views.delete_null_code, name='delete_null'),
]
