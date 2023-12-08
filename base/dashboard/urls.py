from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminDashborad, name='adminDashboard'),
    path('complaints/', views.complaints, name='complaints'),
    path('<str:pk>/showComplaint/', views.showComplaint, name='showComplaint'),
    path('<str:pk>/tokenAccepted/', views.tokenAccepted, name='tokenAccepted'),
]