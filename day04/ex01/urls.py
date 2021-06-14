
from django.urls import include, path
from . import views

urlpatterns = [
    # path('ex00/',ex00.views.index, name='index'),
    path('django', views.renderDjango, name='django'),
    path('display', views.renderDisplay, name='display'),
    path('templates', views.renderTemplates, name='templates'),
]
