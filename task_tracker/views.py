from django.shortcuts import render
from .models import Task
from config.settings import BASE_DIR


def show_all_tasks(request):
    tasks = Task.objects.prefetch_related("comments__task").prefetch_related("tags__tasks").select_related("project").all()
    context = {
        "tasks" : tasks,
    }
    return render(request,"tasks.html",context=context)
