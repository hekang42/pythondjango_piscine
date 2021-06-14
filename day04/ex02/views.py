from django.shortcuts import render
# Create your views here.
from .forms import PersonForm
from .utils import hist, log
from django.http import HttpResponseRedirect
# def renderform(request):
#     return render(request, 'form.html')

def form_test(request):
    return render(request, 
    'history.html', 
    {
        "form": PersonForm(),
        "history": hist(),
    }
    )


def post(request):
    if request.method == "POST":
        if PersonForm(request.POST).is_valid():
            log(request.POST.get("content"))
        return HttpResponseRedirect("/ex02")
