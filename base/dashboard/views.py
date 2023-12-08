from django.shortcuts import render
import users.models
from django.http import HttpResponse

# Create your views here.

# Fuction to Load Dashboard of the Admin

def adminDashborad(request):
    
    return render(request, 'admin/dashboard.html')

# Function to Load the Complaints to the user

def complaints(request):
    if request.user.is_superuser:
        data = users.models.ComplaintForm.objects.all()

        context = {
            'complaints': data
        }
    else:
        return HttpResponse("You Are Not Authorized....")
    return render(request, 'admin/complaints.html', context)