from django.shortcuts import render
 
# Create your views here.
def index(request):
    listd = [i * 5 for i in range(0,50)]
    return render(request, 'gradation.html', { "colors" : listd})