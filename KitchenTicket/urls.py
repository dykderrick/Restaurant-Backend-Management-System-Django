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
    path('edit_status/<str:order_id>/<str:dish_id>/<str:new_status>', views.edit_status, name="edit"),
]
