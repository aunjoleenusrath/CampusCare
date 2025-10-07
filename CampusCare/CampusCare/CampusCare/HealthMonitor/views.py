# views.py in your HealthMonitor app (e.g., campusapp/views.py)

from django.shortcuts import render, redirect, get_object_or_404
from .models import HealthMonitor
from .forms import HealthMonitorForm

def list_health_monitor(request):
    monitors = HealthMonitor.objects.all()
    return render(request, 'healthmonitor/list_health_monitor.html', {'monitors': monitors})

def add_health_monitor(request):
    if request.method == 'POST':
        form = HealthMonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_health_monitor')
    else:
        form = HealthMonitorForm()
    return render(request, 'healthmonitor/add_health_monitor.html', {'form': form})

def update_health_monitor(request, id):
    monitor = get_object_or_404(HealthMonitor, id=id)
    form = HealthMonitorForm(request.POST or None, instance=monitor)
    if form.is_valid():
        form.save()
        return redirect('list_health_monitor')
    return render(request, 'healthmonitor/update_health_monitor.html', {'form': form})

def delete_health_monitor(request, id):
    monitor = get_object_or_404(HealthMonitor, id=id)
    if request.method == 'POST':
        monitor.delete()
        return redirect('list_health_monitor')
    return render(request, 'healthmonitor/delete_health_monitor.html', {'monitor': monitor})

