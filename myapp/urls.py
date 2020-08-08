from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<path1>/<path2>/<path3>/<name>', views.getPage1),     #3层结构
    path('page/<path1>/<path2>/<name>', views.getPage2),             #2层结构
    path('page/<path1>/<name>', views.getPage3),                     #1层结构
]