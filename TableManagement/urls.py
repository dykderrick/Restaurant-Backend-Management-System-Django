# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2
# @Author  : Yingke Ding
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'TableManagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit_table/<str:oid>/<int:capacity>/<str:status>/', views.edit_table, name='edit'),
]
