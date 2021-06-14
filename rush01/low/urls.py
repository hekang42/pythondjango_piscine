from django.urls import path
from .views import * 

from django.conf import settings
from django.conf.urls.static import static
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
        "articles/<int:article_id>/",
        Detail.as_view(),
        name="detail",
    ),
    path('favourite/', Favourites.as_view(), name='favourite'),
    path('publish/', Publish.as_view(), name='publish'),
    path('articles/<int:article_id>/comment/', Detail.as_view(), name="create_comment"),
    path('articles/<int:article_id>/comment/<int:comment_id>', Recomment.as_view(), name="recomment"),
    # path('profile/', Profile_view.as_view(), name='profile'),
    path('profile/', Profile.as_view(), name='profile'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
