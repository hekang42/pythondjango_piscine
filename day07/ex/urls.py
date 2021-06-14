from django.urls import path
from .views import * 

from django.shortcuts import redirect
# from .views import TipCreateView, TipListView, TipDeleteView
urlpatterns = [

    path('articles/', ArticleListView.as_view(), name = 'articles'),
    path('', ArticleRedirectView.as_view(), name = 'index'),
    path('login/', Login.as_view(), name = 'login'),
    path('register/', Registration.as_view(), name = 'register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('publications/', Publications.as_view(), name='publications'),
    path(
        "articles/<slug:pk>/",
        Detail.as_view(),
        name="detail",
    ),
    path('favourite/', Favourites.as_view(), name='favourite'),
    path('publish/', Publish.as_view(), name='publish'),


    ]