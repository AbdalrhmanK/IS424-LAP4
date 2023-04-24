from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('/taxrate' , views.taxrate , name='taxrate'),
    path('/<str:number>' , views.anyNumber , name='anyNumber'),

]