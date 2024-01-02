from django.shortcuts import render, redirect
from List.forms import ToDoForm
from List.models import ToDoModel

def home(request):
    return render(request, 'home.html')

def show_tasks(request):
    tasks = ToDoModel.objects.filter(status = False)
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
    task = ToDoModel.objects.get(pk=id)
    form = ToDoForm(instance=task)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'add_tasks.html', {'form': form})

def delete_task(request, id):
    task = ToDoModel.objects.get(pk=id).delete()
    return redirect('show_tasks')

def complete_task(request, id):
    task = ToDoModel.objects.get(pk=id)
    task.status = False
    task.save()
    return redirect('completed_tasks')

def completed_tasks(request):
    completed_tasks = ToDoModel.objects.filter(status=False)
    return render(request, 'completed_tasks.html', {'data': completed_tasks})

def complete_delete_task(request, id):
    task = ToDoModel.objects.get(pk=id).delete()
    return redirect('completed_tasks')
