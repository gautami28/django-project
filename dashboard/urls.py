from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name="home"),
    path('dictionary/',views.dictionary,name="dictionary"),
    path('translate/', views.translate_app, name='trans'),
    path('conversion/',views.conversions,name="conversion"),
    path('wiki/',views.wiki,name="wiki"),
]
