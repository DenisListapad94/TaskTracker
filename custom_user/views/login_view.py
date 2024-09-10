import json

from django.views import View
from django.http.response import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout

User = get_user_model()


def own_logout(request):
    logout(request)
    return JsonResponse({'logout': 'success'})


class LoginView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        user = authenticate(request, **user_data)
        if user:
            login(request, user)
        return JsonResponse(model_to_dict(user))
