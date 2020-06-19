from django.urls import path
from . import views

app_name = 'devdata'

urlpatterns = [
    path('',views.index,name='index'),
]