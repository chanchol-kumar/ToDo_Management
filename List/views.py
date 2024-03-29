from django.shortcuts import render, redirect
from List.forms import ToDoForm
from List.models import TaskModel

def home(request):
    return render(request, 'home.html')

def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed = False)
    return render(request, 'show_tasks.html', {'data': tasks})

def add_tasks(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = ToDoForm()
    return render(request, 'add_tasks.html', {'form': form})

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = ToDoForm(instance=task)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_tasks.html', {'form': form})

def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_tasks')

def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'data': completed_tasks})

def complete_delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('completed_tasks')