from django.contrib import admin
from django.urls import path, include


from base.views import (
    MainPageView, LoginTemplateView
)
from base.views.main_page_view import some_view

urlpatterns = [
    path('', MainPageView.as_view()),
    path('login/', LoginTemplateView.as_view()),
    path('view/',some_view)
]
