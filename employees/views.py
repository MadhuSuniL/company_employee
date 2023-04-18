from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Employee
from .forms import EmployeeForm

def home(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'employees/home.html', context)

def add_employee(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
            return redirect('employees:home')
    else:
        form = EmployeeForm()
    context = {'company': company, 'form': form}
    return render(request, 'employees/add_employee.html', context)
