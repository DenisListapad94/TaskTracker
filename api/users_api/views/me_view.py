from django.views import View

from django.http.response import JsonResponse

from django.forms.models import model_to_dict


class MeView(View):
    def get(self, request):
        return JsonResponse(
            model_to_dict(request.user),
            status=200
        )
