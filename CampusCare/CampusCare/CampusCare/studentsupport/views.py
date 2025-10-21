from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentSupport
from .forms import StudentSupportForm


def add_support(request):
    if request.method == 'POST':
        form = StudentSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_student_supports')  # ✅ Correct redirect
    else:
        form = StudentSupportForm()
    return render(request, 'studentsupport/add_supportt.html', {'form': form})


def list_supports(request):
    supports = StudentSupport.objects.all()
    return render(request, 'studentsupport/list_supportss.html', {'supports': supports})


def update_support(request, id):
    support = get_object_or_404(StudentSupport, id=id)
    form = StudentSupportForm(request.POST or None, instance=support)
    if form.is_valid():
        form.save()
        return redirect('list_student_supports')  # ✅ Correct redirect
    return render(request, 'studentsupport/update_supportt.html', {'form': form})


def delete_support(request, id):
    support = get_object_or_404(StudentSupport, id=id)
    if request.method == 'POST':
        support.delete()
        return redirect('list_student_supports')  # ✅ Correct redirect
    return render(request, 'studentsupport/delete_supportt.html', {'support': support})