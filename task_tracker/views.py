from django.shortcuts import render, redirect,reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

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


class TasksTemplateView(ListView,PermissionRequiredMixin):
    permission_required = "task_tracker.view_task"
    template_name = "tasks.html"
    model = Task

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["tasks"] = Task.objects.prefetch_related("comments__task") \
    #         .prefetch_related("tags__tasks") \
    #         .select_related("project") \
    #         .all()
    #     return context


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


class TaskFormView(FormView):
    template_name = "task_form.html"
    form_class = TaskModelForm
    success_url = reverse_lazy("all_tasks")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
