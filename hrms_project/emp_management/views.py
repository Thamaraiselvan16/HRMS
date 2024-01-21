from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from django.http import HttpResponse
from .forms import EmployeeForm
import csv
from django.utils import timezone
from django.db import IntegrityError
# from reportlab.pdfgen import canvas
# from django.db.models import Count
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Create your views here.

# all employee list
def employee_list(request):
    employees = Employee.objects.all()
    total_department_count = employees.values('department').distinct().count()
    return render(request, 'emp_management/employee_list.html', {'employees': employees, 'total_department_count': total_department_count})

# add a new employee
def add_employee(request):
    message = ''

    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        date_of_joining = request.POST.get('date_of_joining')

        # Convert the input date_of_joining to a Python date object
        date_of_joining = timezone.datetime.strptime(date_of_joining, '%Y-%m-%d').date()

        # Ensure date_of_joining is less than or equal to the current date
        if date_of_joining > timezone.now().date():
            message = 'Error: Date of joining must be less than or equal to the current date.'
        else:
            try:
                Employee.objects.create(
                    name=name,
                    designation=designation,
                    department=department,
                    date_of_joining=date_of_joining
                )
                message = 'Employee added successfully!'
                return redirect('employee_list')
            except IntegrityError:
                message = 'Error: Employee with this name already exists.'

    return render(request, 'emp_management/add_employee.html', {'message': message})

# download pdf format
# def employee_list_pdf(request):
#     # A4 dimensions in pixels
#     a4_width, a4_height = 595.276, 841.890

#     employees = Employee.objects.all()

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="employee_list.pdf"'

#     # Create the PDF object, using the response object as its "file."
#     pdf_buffer = HttpResponse(content_type='application/pdf')
#     pdf_buffer['Content-Disposition'] = 'attachment; filename="employee_list.pdf"'

#     # Create the PDF object, using the response object as its "file."
#     pdf = SimpleDocTemplate(pdf_buffer, pagesize=(a4_width, a4_height))

#     # Add content to the PDF here
#     data = [['Name', 'Department', 'Designation', 'Date of Joining']]
#     for employee in employees:
#         data.append([employee.name, employee.department, employee.designation, str(employee.date_of_joining)])

#     # Create the table
#     table = Table(data, colWidths=[150, 150, 150, 150])

#     # Add style to the table
#     style = TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black)
#     ])
#     table.setStyle(style)

#     # Build the PDF
#     elements = [table]
#     pdf.build(elements)

#     return pdf_buffer


# download csv format
def employee_list_csv(request):
    employees = Employee.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee_list.csv"'

    # Create the CSV writer using the response object as its "file."
    csv_writer = csv.writer(response)

    # Write the header row
    csv_writer.writerow(['Name', 'Department', 'Designation', 'Date of Joining'])

    # Write the data rows
    for employee in employees:
        csv_writer.writerow([employee.name, employee.department, employee.designation, employee.date_of_joining.strftime('%Y-%m-%d')])

    return response

# Updation of employee
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'emp_management/update_employee.html', {'form': form, 'employee': employee})

# Deletion of employee
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'emp_management/delete_employee.html', {'employee': employee})