from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_supports, name='list_student_supports'),
    path('add/', views.add_support, name='add_student_support'),
    path('update/<int:id>/', views.update_support, name='update_student_support'),
    path('delete/<int:id>/', views.delete_support, name='delete_student_support'),
]