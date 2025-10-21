from django.shortcuts import render, redirect, get_object_or_404
from .models import MentalSupport
from .forms import MentalSupportForm


def add_support(request):
    if request.method == 'POST':
        form = MentalSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mentalsupport:list_supports')  # ✅ fixed
    else:
        form = MentalSupportForm()
    return render(request, 'mentalsupport/add_support.html', {'form': form})

def list_supports(request):
    supports = MentalSupport.objects.all()
    return render(request, 'mentalsupport/list_supports.html', {'services': supports})

def update_support(request, id):
    support = get_object_or_404(MentalSupport, id=id)
    form = MentalSupportForm(request.POST or None, instance=support)
    if form.is_valid():
        form.save()
        return redirect('mentalsupport:list_supports')  # ✅ fixed
    return render(request, 'mentalsupport/update_support.html', {'form': form})

def delete_support(request, id):
    support = get_object_or_404(MentalSupport, id=id)
    if request.method == 'POST':
        support.delete()
        return redirect('mentalsupport:list_supports')  # ✅ fixed
    return render(request, 'mentalsupport/delete_support.html', {'support': support})
