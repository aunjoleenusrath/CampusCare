from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_monitors, name='list_monitorss'),
    path('add/', views.add_monitor, name='add_monitor'),
    path('update/<int:id>/', views.update_monitor, name='update_monitor'),
    path('delete/<int:id>/', views.delete_monitor, name='delete_monitor'),
]
