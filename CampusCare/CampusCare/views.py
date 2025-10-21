# home/views.py
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'home/index.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # (For now, just simulate login)
        # In a real app, you'd authenticate user here
        if email and password:
            return redirect('diseases_page')
        else:
            return render(request, 'home/login.html', {'error': 'Invalid credentials'})

    return render(request, 'home/login.html')

def signup_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # (Simulated registration)
        if full_name and email and password:
            return redirect('login_page')
        else:
            return render(request, 'home/signup.html', {'error': 'Please fill all fields'})

    return render(request, 'home/signup.html')

def diseases_page(request):
    return render(request, 'home/diseases.html')

from django.shortcuts import render

def payment_page(request):
    item = request.GET.get("item", "Unknown")
    price = request.GET.get("price", "—")
    return render(request, 'home/payment.html', {"item": item, "price": price})

def payment_gateway(request):
    item = request.GET.get("item", "Unknown")
    price = request.GET.get("price", "—")
    return render(request, 'home/payment_gateway.html', {"item": item, "price": price})

def payment_gateway(request):
    item = request.GET.get("item", "Unknown")
    price = request.GET.get("price", "—")
    return render(request, 'home/payment_gateway.html', {"item": item, "price": price})
