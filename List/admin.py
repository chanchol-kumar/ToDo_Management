from django.contrib import admin
from List.models import ToDoModel

class ToDoModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')

admin.site.register(ToDoModel, ToDoModelAdmin)