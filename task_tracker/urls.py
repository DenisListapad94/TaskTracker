from django.urls import path

from task_tracker.views import show_all_tasks,create_task_form

urlpatterns = [
    path('',show_all_tasks,name="all_tasks"),
    path('create',create_task_form)
]
