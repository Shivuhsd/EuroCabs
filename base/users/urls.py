from django.urls import path
from . import views

urlpatterns = [
#     path('/', views.adminDashborad, name='adminDashboard'),
    #Complaint Endpoint

    path('complaintForm/', views.complaintForm, name='complaintForm'),
]