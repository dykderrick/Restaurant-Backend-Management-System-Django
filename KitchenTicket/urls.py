# -*- coding: utf-8 -*-
# @Time    : 4/6/21 14:17
# @Author  : Yingke Ding
# @FileName: urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'KitchenTicket'
urlpatterns = [
    path('', views.index, name="index"),
]
