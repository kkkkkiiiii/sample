from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
    path('result/', views.result, name='result'),
    path('add/', views.add, name='add')

]
