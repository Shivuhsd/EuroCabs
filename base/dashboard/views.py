from django.shortcuts import render, redirect
import users.models
from django.http import HttpResponse, JsonResponse

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


# Function to Display the Complaint to Admin

def showComplaint(request, pk):
    try:
        data = users.models.ComplaintForm.objects.get(id = pk)

        context = {
            'data': data
        }
        return render(request, 'admin/showComplaint.html', context)
    except:
        return custom404(request)

#Function To Accept the Token

def tokenAccepted(request, pk):
    try:
        data = users.models.ComplaintForm.objects.get(id = pk)
        data.opened = True
        data.save()
        return JsonResponse({'status': 'success'})
    except:
        return JsonResponse({'status': 'failed'})
   



def custom404(request, exception = None):
    return render(request, 'admin/404.html', status=404)