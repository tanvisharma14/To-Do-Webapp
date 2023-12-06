from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST["task"]
    Task.objects.create(task=task)
    return redirect("home")

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = True
    task.save()
    return redirect("home")

def markAsUndone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = False
    task.save()
    return redirect("home")

def editTask(request, pk):
    getTask = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        newTask = request.POST["task"]
        getTask.task = newTask
        getTask.save()
        return redirect("home")
    else:
        context = {
            "getTask": getTask,
        }
        return render(request, "editTask.html", context)
    
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")