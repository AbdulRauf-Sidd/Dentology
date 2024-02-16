from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patients),
    path('patients/<int:pk>', views.single_patient),
]