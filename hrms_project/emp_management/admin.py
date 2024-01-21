from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department', 'date_of_joining')
    list_filter = ('designation', 'department', 'date_of_joining')
    search_fields = ('name', 'department', 'date_of_joining__year')
    date_hierarchy = 'date_of_joining'
    ordering = ('-date_of_joining',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'designation', 'department')
        }),
        ('Joining Information', {
            'fields': ('date_of_joining',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['date_of_joining']
        return []

admin.site.register(Employee, EmployeeAdmin)
