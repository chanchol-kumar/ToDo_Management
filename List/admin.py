from django.contrib import admin
from List.models import TaskModel

class ToDoModelAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription', 'is_completed')

admin.site.register(TaskModel, ToDoModelAdmin)