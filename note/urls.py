#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：clode_node 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：komorebi
@Email   ：komorebi.so.67@gmail.com
@Date    ：2025/1/1 9:52 
'''

from django.urls import path

from note import views

urlpatterns = [
    path('', views.list_view,name="noteList"),
    path('add/', views.add_view),
    path('mod/<id>/', views.mod_view,name="mod"),
    path('del/<id>', views.del_view),
]