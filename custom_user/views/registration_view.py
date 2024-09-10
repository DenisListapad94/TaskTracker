import json

from django.views import View
from django.http.response import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        user = User.objects.create_user(**user_data)
        return JsonResponse(model_to_dict(user))
