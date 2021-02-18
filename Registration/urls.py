# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3
# @Author  : Yingke Ding
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'Registration'
urlpatterns = [
    path('<str:table_number>', views.index, name='index'),
]