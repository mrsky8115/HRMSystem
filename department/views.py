from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from django.contrib import messages
from .forms import DepartmentForm

def department_list(request):
    departments = Department.objects.filter(status=True)
    context = {
        'departments': departments,
        'no_data_message': "No departments available." if not departments else None
    }
    return render(request, 'department_list.html', context)

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

def edit_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'edit_department.html', {'form': form})


def delete_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    department.status = False
    department.save()
    messages.success(request, "Department has been marked as inactive.")
    return redirect('department_list')