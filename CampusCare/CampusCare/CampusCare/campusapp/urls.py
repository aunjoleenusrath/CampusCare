from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_services, name='list_services'),
    path('add/', views.add_service, name='add_service'),
    path('update/<int:id>/', views.update_service, name='update_service'),
    path('delete/<int:id>/', views.delete_service, name='delete_service'),
]


