from django.urls import path
from .views import * 
# from .views import TipCreateView, TipListView, TipDeleteView
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('tip/', Tip.as_view(), name='tip'),
    ]