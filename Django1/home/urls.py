from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('/top', views.top, name='top'),
    path('/galeria', views.gallery, name='galeria')
]
