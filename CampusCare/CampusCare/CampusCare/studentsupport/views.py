# --------------------------------------------------------
# Django Views for Student Support Management
# --------------------------------------------------------
# Purpose:
#   Handle all CRUD (Create, Read, Update, Delete) operations
#   for the StudentSupport model in the Campus Care project.
# --------------------------------------------------------


from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentSupport
from .forms import StudentSupportForm



#Create add_support function
def add_support(request):
    if request.method == 'POST':
        form = StudentSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_student_supports')  # ✅ Correct redirect
    else:
        form = StudentSupportForm()
    return render(request, 'studentsupport/add_supportt.html', {'form': form})

#Create list_supports function
def list_supports(request):
    supports = StudentSupport.objects.all()
    return render(request, 'studentsupport/list_supportss.html', {'supports': supports})

#Create update_supports function
def update_support(request, id):
    support = get_object_or_404(StudentSupport, id=id)
    form = StudentSupportForm(request.POST or None, instance=support)
    if form.is_valid():
        form.save()
        return redirect('list_student_supports')  # ✅ Correct redirect
    return render(request, 'studentsupport/update_supportt.html', {'form': form})

#Create delete_supports function
def delete_support(request, id):
    support = get_object_or_404(StudentSupport, id=id)
    if request.method == 'POST':
        support.delete()
        return redirect('list_student_supports')  # ✅ Correct redirect
    return render(request, 'studentsupport/delete_supportt.html', {'support': support})







# --------------------------------------------------------
# End of Views File
# Notes:
# - Each function corresponds to one CRUD operation.
# - Django forms handle input validation and database saving.
# - get_object_or_404 ensures safety by raising HTTP 404 for invalid IDs.
# - Templates should match the paths specified in the render() calls.
# --------------------------------------------------------