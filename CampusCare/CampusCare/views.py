from django.shortcuts import render, redirect, get_object_or_404
from .models import HealthMonitor
from .forms import HealthMonitorForm


def add_monitor(request):
    if request.method == 'POST':
        form = HealthMonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_monitors')
    else:
        form = HealthMonitorForm(])
    return render(request, 'healthmonitor/add_monitor.html', {'form': form})


def list_monitors(request):
    monitors = HealthMonitor.objects.all()
    return render(request, 'healthmonitor/list_monitors.html', {'monitors': monitors})


def update_monitor(request, id):
    monitor = get_object_or_404(HealthMonitor, id=id)
    form = HealthMonitorForm(request.POST or None, instance=monitor)
    if form.is_valid():
        form.save()
        return redirect('list_monitors')
    return render(request, 'healthmonitor/update_monitor.html', {'form': form})


def delete_monitor(request, id):
    monitor = get_object_or_404(HealthMonitor, id=id)
    if request.method == 'POST':
        monitor.delete()
        return redirect('list_monitors')
    return render(request, 'healthmonitor/delete_monitor.html', {'monitor': monitor})
