from django.shortcuts import render, redirect
from taskmanager.models import TaskList
from taskmanager.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.manage = request.user
            task.save()
        messages.success(request, 'new Task Added')
        return redirect('todolist')

    else:
        allTasks = TaskList.objects.filter(manage=request.user)
        p = Paginator(allTasks, 5)
        page = request.GET.get('page')
        allTasks = p.get_page(page)
        return render(request, 'task.html',  {"tasklist": allTasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, 'This action Not Allowed')
    return redirect('todolist')


def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ' Task edited')
        return redirect('todolist')

    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html',  {"task_obj": task_obj})


def about(request):
    context = {'h1_txt': 'This is about us'}
    return render(request, 'about.html',  context)


def contact(request):
    context = {'h1_txt': 'This is contact us'}
    return render(request, 'contact.html',  context)


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, 'This action Not Allowed')
    return redirect('todolist')


def uncomplete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


def index(request):
    context = {'index_text': 'This is Index Page'}
    return render(request, 'index.html',  context)
