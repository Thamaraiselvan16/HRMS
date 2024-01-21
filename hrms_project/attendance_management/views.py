from django.shortcuts import render, get_object_or_404,redirect
from .models import Attendance
from emp_management.models import Employee
from django.utils import timezone
from attendance_management.models import Attendance  

# mark attendance fro individual employee
def mark_attendance(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        date_str = request.POST.get('date')
        status = request.POST.get('status')

        # Convert the date string to a Python date object
        date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()

        # Check if an attendance record already exists for the given date and employee
        existing_attendance = Attendance.objects.filter(employee=employee, date=date)

        if existing_attendance.exists():
            # If an attendance record already exists, you might want to handle it (e.g., show an error message)
            error_message = f"Attendance record for {employee.name} on {date_str} already exists."
            return render(request, 'attendance_management/mark_attendance.html', {'employee': employee, 'error_message': error_message})
        elif date > timezone.now().date():
            # If the date is in the future, you might want to handle it (e.g., show an error message)
            error_message = "Date should be less than or equal to the current date."
            return render(request, 'attendance_management/mark_attendance.html', {'employee': employee, 'error_message': error_message})
        else:
            # Create a new attendance record
            Attendance.objects.create(employee=employee, date=date, status=status)
            return redirect('employee_list')

    return render(request, 'attendance_management/mark_attendance.html', {'employee': employee})

# attendance details of individual employee
def attendance_details(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    attendance_details = Attendance.objects.filter(employee=employee)

    return render(request, 'attendance_management/attendance_details.html', {'employee': employee, 'attendance_details': attendance_details})