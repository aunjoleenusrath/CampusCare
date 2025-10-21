from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_supports, name='list_supports'),
    path('add/', views.add_support, name='add_support'),
    path('update/<int:id>/', views.update_support, name='update_support'),
    path('delete/<int:id>/', views.delete_support, name='delete_support'),
]
