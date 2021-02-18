# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/20
# @Author  : Yingke Ding
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'MenuManagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_dish/', views.add_dish, name='add'),
    path('edit_dish/<str:oid>/', views.edit_dish, name='edit'),
    path('delete_dish/<str:oids>/', views.delete_dish, name='delete'),
    path('delete_dish/', views.delete_null_dish, name='delete_null'),
]
