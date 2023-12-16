from django.urls import path, re_path
from . import views
from .views import search 

app_name = "mainapp"

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('home/', views.home, name='home'),
    path('test/', views.test, name='test'),
    path("search/<tid>", views.search, name='search'),
    path("patientlist/<tid>", views.patientlist, name="patientlist"),
    #re_path('r^search/(?P<id>\d+)/$', search.as_view(), name='search'),
]