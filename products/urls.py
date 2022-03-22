from django.urls import path
from . import views # Period. means import views.py at current folder


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]