from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        messages.success(request, ("New Task Added"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Denied."))
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if task.owner == request.user:
            if form.is_valid():   
                form.save()   
            messages.success(request, ("Task Edited"))
        else:
            messages.error(request, ("Access Denied."))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Denied."))
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ("Access Denied."))
    return redirect('todolist')

def index(request):
    context = {
        'index_text': 'Welcome to Index Page',
        }
    return render(request, 'index.html', context)

def contact(request):
    context = {
        'contact_header': 'Welcome to Contact Page',
        'contact_text': "You can reach me at ",
        'contact_email': 'artem.ramus@gmail.com',
        }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_header': 'Welcome to About Page',
        'about_text': 'Artem Ramus, Data Scientist and Backend Developer',
        }
    return render(request, 'about.html', context)