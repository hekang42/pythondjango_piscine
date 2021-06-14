from django.views.generic import RedirectView
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

class Logout(RedirectView):
    url = "index.html"

    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('index')