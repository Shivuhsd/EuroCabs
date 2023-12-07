from django.shortcuts import render

# Create your views here.

# Fuction to Load Dashboard of the Admin

def adminDashborad(request):
    return render(request, 'admin/dashboard.html')