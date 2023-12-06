from django.shortcuts import render
from toDo.models import Task

def home(request):
    tasks = Task.objects.filter(isCompleted = False).order_by("-updatedAt")
    completedTasks = Task.objects.filter(isCompleted = True)
    context = {
        "tasks": tasks,
        "completedTasks": completedTasks
    }
    return render(request, "home.html", context)