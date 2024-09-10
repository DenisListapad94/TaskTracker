from django.views import View

from django.http.response import JsonResponse

from django.contrib.auth import logout


class LogOutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse(
            {'logout': 'success'},
            status=200
        )
