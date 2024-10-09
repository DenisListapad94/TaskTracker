from django.urls import path

from api.tasks_api.views.tasks_view import TaskList,TaskDetail

urlpatterns = [
    path('', TaskList.as_view()),
    path('<int:pk>',TaskDetail.as_view())
]
