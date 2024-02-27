from django.contrib import admin
from .models import Task, Group

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed', 'priority', 'created_at', 'updated_at', 'group')

admin.site.register(Task, TaskAdmin)
admin.site.register(Group)
