from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('send_request/', views.get_request, name='exec'),
]