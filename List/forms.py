from django import forms
from List.models import TaskModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
