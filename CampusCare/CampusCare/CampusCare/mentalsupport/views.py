from django.shortcuts import render, redirect, get_object_or_404
from .models import MentalSupport
from .forms import MentalSupportForm

# CREATE
def add_support(request):
    if request.method == 'POST':
        form = MentalSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_supports')
    else:
        form = MentalSupportForm()
    return render(request, 'mentalsupport/add_support.html', {'form': form})

# READ
def list_supports(request):
    supports = MentalSupport.objects.all()
    return render(request, 'mentalsupport/list_supports.html', {'supports': supports})

# UPDATE
def update_support(request, id):
    support = get_object_or_404(MentalSupport, id=id)
    form = MentalSupportForm(request.POST or None, instance=support)
    if form.is_valid():
        form.save()
        return redirect('list_supports')
    return render(request, 'mentalsupport/update_support.html', {'form': form})

# DELETE
def delete_support(request, id):
    support = get_object_or_404(MentalSupport, id=id)
    if request.method == 'POST':
        support.delete()
        return redirect('list_supports')
    return render(request, 'mentalsupport/delete_support.html', {'support': support})
