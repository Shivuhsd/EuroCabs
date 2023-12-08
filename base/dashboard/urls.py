from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminDashborad, name='adminDashboard'),
    path('complaints/', views.complaints, name='complaints'),
]