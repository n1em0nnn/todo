from turtledemo.paint import switchupdown
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.contrib.auth.models import User
from .models import Task

# Create your views here.
@login_required(login_url="/login/")
def get_tasks(request):
    user = request.user
    tasks = Task.objects.all()
    return render(request,"task/index.html",{"tasks":tasks, "user":user})
@login_required(login_url="/login/")
def add_task(request):
    if request.method == "POST":
        Task.objects.create(
            title = request.POST.get("title"),
            descr = request.POST.get("descr")
        )
    return redirect('task_list')
@login_required(login_url="/login/")
def edit_task(request,id):
    task = get_object_or_404(Task,id=id)
    return render(request,'task/edit.html',{'task':task})
@login_required(login_url="/login/")
def update_task(request,id):
    if request.method == "POST":
        task = get_object_or_404(Task,id=id)
        task.title = request.POST.get("title")
        task.descr = request.POST.get("descr")
        task.status = request.POST.get("status")
        task.save()
    return redirect('task_list')
@login_required(login_url="/login/")
def delete_task(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.delete()
    return redirect('task_list')