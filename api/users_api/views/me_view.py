from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.views import View


class MeView(View):
    def get(self, request):
        return JsonResponse(
            model_to_dict(request.user),
            status=200
        )
