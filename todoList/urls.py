"""djangoProject7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todoList import views

urlpatterns = [
    path('', views.task_view, name='task_view'),
    path('search_tasks', views.search_tasks, name='search_tasks'),
    path('add', views.add_new_tasks, name='add_new_task'),
    path('update_list/<int:id>', views.update_list, name='update_list'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
]
