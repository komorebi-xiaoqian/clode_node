#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：clode_node 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：komorebi
@Email   ：komorebi.so.67@gmail.com
@Date    ：2025/1/1 9:50 
'''
from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('reg/', views.reg_view),
    path('logout/', views.logout_view),
]
