from django.shortcuts import render
from .models import Task
from config.settings import BASE_DIR


def show_all_tasks(request):
    tasks = Task.objects.all()
    context = {
        "tasks" : tasks,
        "base_dir": BASE_DIR
    }
    return render(request,"tasks.html",context=context)
