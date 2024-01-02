from django.urls import path
from List.views import home, add_tasks, show_tasks, edit_task, delete_task, complete_task, completed_tasks,complete_delete_task

urlpatterns = [
    path('', home, name='homepage'),
    path('add_tasks/', add_tasks, name='add_tasks'),
    path('show_tasks/', show_tasks, name='show_tasks'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('complete_task/<int:id>/', complete_task, name='complete_task'),
    path('complete_delete_task/<int:id>/', complete_delete_task, name='complete_delete_task'),
    path('completed_tasks/', completed_tasks, name='completed_tasks'),
]
