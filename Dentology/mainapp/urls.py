from django.urls import path, re_path
from . import views
from .views import search
# urls.py

from django.conf import settings
from django.conf.urls.static import static

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


app_name = "mainapp"

urlpatterns = [
    path('', views.test, name = "none"),
    path('login/', views.login, name = 'login'),
    path('home/', views.home, name='home'),
    path('test/', views.test, name='test'),
    path("search/<tid>", views.search, name='search'),
    path("addpatient/", views.addpatient, name='addpatient'),
    path("patientlist/<tid>", views.patientlist, name="patientlist"),
    path("edittooth/<pid>/", views.edittooth1, name="teethlist"),
    path("edittooth/<pid>/<tid>", views.edittooth2, name="edittooth"),
    path("test/", views.test, name="edittooth"),
    #re_path('r^search/(?P<id>\d+)/$', search.as_view(), name='search'),
]