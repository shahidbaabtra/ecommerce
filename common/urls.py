from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.master, name="master"),
    path('', views.index, name="index"),
]