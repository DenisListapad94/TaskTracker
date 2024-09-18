from time import sleep

from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Task


@cache_page(120, cache="default", key_prefix="tasks")
def show_all_tasks(request):
    tasks = Task.objects.prefetch_related("comments__task").prefetch_related("tags__tasks").select_related(
        "project").all()
    context = {
        "tasks": tasks,
    }
    sleep(10)
    return render(request, "tasks.html", context=context)
