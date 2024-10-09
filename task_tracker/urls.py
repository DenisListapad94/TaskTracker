from django.urls import path

from task_tracker.views import show_all_tasks,create_task_form,TasksTemplateView,TaskFormView

urlpatterns = [
    path('',TasksTemplateView.as_view(),name="all_tasks"),
    path('create',TaskFormView.as_view(),name="create_task")
]
