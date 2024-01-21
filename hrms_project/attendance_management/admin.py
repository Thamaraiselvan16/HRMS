from django.contrib import admin
from .models import Attendance

# it will show on admin page "superuser"
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'date', 'employee__department')  # Filter by status, date, and employee department
    search_fields = ('employee__name', 'date')  # Search by employee name and date
    date_hierarchy = 'date'  # Add a date hierarchy navigation
    ordering = ('-date',)  # Order by date descending

    def get_readonly_fields(self, request, obj=None):
        # Make the 'employee' field readonly once the Attendance record is created
        if obj:
            return ['employee']
        return []

admin.site.register(Attendance, AttendanceAdmin)
