from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalService
from .forms import MedicalServiceForm

# CREATE
def add_service(request):
    if request.method == 'POST':
        form = MedicalServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_services')
    else:
        form = MedicalServiceForm()
    return render(request, 'add_service.html', {'form': form})

# READ
def list_services(request):
    services = MedicalService.objects.all()
    return render(request, 'list_services.html', {'services': services})

# UPDATE
def update_service(request, id):
    service = get_object_or_404(MedicalService, id=id)
    form = MedicalServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('list_services')
    return render(request, 'update_service.html', {'form': form})

# DELETE
def delete_service(request, id):
    service = get_object_or_404(MedicalService, id=id)
    if request.method == 'POST':
        service.delete()
        return redirect('list_services')
    return render(request, 'delete_service.html', {'service': service})
