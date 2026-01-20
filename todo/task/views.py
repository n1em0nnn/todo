from turtledemo.paint import switchupdown

from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request

from .models import Task

# Create your views here.

def get_tasks(request):
    tasks = Task.objects.all()
    return render(request,"task/index.html",{"tasks":tasks})
def add_task(request):
    if request.method == "POST":
        Task.objects.create(
            title = request.POST.get("title"),
            descr = request.POST.get("descr")
        )
    return redirect('task_list')
def edit_task(request,id):
    task = get_object_or_404(Task,id=id)
    return render(request,'task/edit.html',{'task':task})
def update_task(request,id):
    if request.method == "POST":
        task = get_object_or_404(Task,id=id)
        task.title = request.POST.get("title")
        task.descr = request.POST.get("descr")
        task.status = request.POST.get("status")
        task.save()
    return redirect('task_list')

def delete_task(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.delete()
    return redirect('task_list')