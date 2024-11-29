from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from custom_user.views import (
    RegistrationView,
    LoginView,
    UserInfoView,
    own_logout,
)

urlpatterns = [
    path('registration/', csrf_exempt(RegistrationView.as_view()), name="register"),
    path('login/', csrf_exempt(LoginView.as_view()), name="login"),
    path('logout/', csrf_exempt(own_logout), name="logout"),
    path('me/', csrf_exempt(UserInfoView)),
]
