# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ✅ matches your view
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('diseases/', views.diseases_page, name='diseases_page'),
    path('payment/', views.payment_page, name='payment_page'),
    path('gateway/', views.payment_gateway, name='payment_gateway'),
]


