from django.http.response import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required


@login_required
def UserInfoView(request):
    return JsonResponse(model_to_dict(request.user))
