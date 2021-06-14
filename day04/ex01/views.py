from django.shortcuts import render

# Create your views here.
def renderDjango(request):
    return render(request, 'django.html')
def renderDisplay(request):
    return render(request, 'display.html')
def renderTemplates(request):
    return render(request, 'templates.html')

    # msg = 'My Message'
    # return render(request, 'index.html', {'message': msg})
    # style = "href=/static/style1.css"
    # usage {{meesage}}