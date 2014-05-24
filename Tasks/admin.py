from django.contrib import admin
from Tasks.models import  Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin): #change the view order in the admin site
    fieldsets = [
        (None,               {'fields': ['name_text','description_text']}),
        ('Other information', {'fields': ['priority'] }),
        ('Date information', {'fields': ['task_date'] , 'classes': ['collapse']}),
    ]
    list_display = ('name_text', 'task_date')

admin.site.register(Task,TaskAdmin)
