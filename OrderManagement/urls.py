# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1
# @Author  : Yingke Ding
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'OrderManagement'
urlpatterns = [
    path('', views.index, name='index'),
]
