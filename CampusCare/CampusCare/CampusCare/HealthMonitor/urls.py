from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_health_monitor, name='list_health_monitor'),
    path('add/', views.add_health_monitor, name='add_health_monitor'),
    path('update/<int:id>/', views.update_health_monitor, name='update_health_monitor'),
    path('delete/<int:id>/', views.delete_health_monitor, name='delete_health_monitor'),
]

