import json

from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login

User = get_user_model()


class LoginView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        user = authenticate(request, **user_data)
        response_json = {
            'data': {'login': 'failed'},
            'status': 401,
        }
        if user:
            login(request, user)
            response_json.update({
                'data': {'login': 'success'},
                'status': 200,
            })
        return JsonResponse(**response_json)
