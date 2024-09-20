from time import sleep

from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_page

from .forms import TaskModelForm
from .models import Task


# @cache_page(120, cache="default", key_prefix="tasks")
def show_all_tasks(request):
    tasks = Task.objects.prefetch_related("comments__task").prefetch_related("tags__tasks").select_related(
        "project").all()
    context = {
        "tasks": tasks,
    }

    return render(request, "tasks.html", context=context)


def create_task_form(request):
    context = {}
    # form = TaskForm()
    if request.method == "POST":

        form = TaskModelForm(request.POST, request.FILES)

        form.save()

        if form.is_valid():
            context["form"] = form

            return redirect("all_tasks")
    else:
        form = TaskModelForm()
        context["form"] = form

    return render(request, "task_form.html", context=context)
