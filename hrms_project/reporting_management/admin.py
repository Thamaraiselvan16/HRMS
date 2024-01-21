from django.contrib import admin
from .models import EmployeeReport

# it will show on admin page "superuser"
class EmployeeReportAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department', 'date', 'status')
    list_filter = ('department', 'date', 'status', 'employee__designation')  # Filter by department, date, status, and employee designation
    search_fields = ('employee__name', 'date')  # Search by employee name and date
    date_hierarchy = 'date'  # Add a date hierarchy navigation
    ordering = ('-date',)  # Order by date descending

    fieldsets = (
        ('Employee Information', {
            'fields': ('employee', 'department')
        }),
        ('Report Information', {
            'fields': ('date', 'status')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        # Make the 'employee' and 'date' fields readonly once the EmployeeReport record is created
        if obj:
            return ['employee', 'date']
        return []

admin.site.register(EmployeeReport, EmployeeReportAdmin)
