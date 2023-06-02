from django.urls import path
from django.contrib import admin

from . import views

app_name = 'polls'

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:question_id>/',views.detail,name='detail'),
    path('admin/', admin.site.urls),

]


