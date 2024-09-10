from django.urls import path

from task_tracker.views import show_all_tasks

urlpatterns = [
    path('',show_all_tasks)
]