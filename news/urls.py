from django.contrib import admin
from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path('',views.news,name = "news"),
    path('addnews/',views.addNews,name = "addnews"),
    path('delete/<int:id>',views.deleteNews,name = "deletenews"),
    path('news/<int:id>',views.newsDetail,name = "newsDetail"),
    path('update/<int:id>',views.updateNews,name = "updatenews"),

]
    
