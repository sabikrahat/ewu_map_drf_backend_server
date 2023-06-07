from django.urls import path
from api_server import views

urlpatterns = [
    path('', views.check, name='check'),
    path('point_detect', views.point_detect, name='point_detect'),
    path('point_detect/', views.point_detect, name='point_detect'),
]