from django.shortcuts import render
from .models import ComplaintForm
# Create your views here.

# Fuction to Get Complaint from user and store it in the Database

def complaintForm(request):
    other = ''
    if request.method == 'POST':
        userName = request.POST['userName']
        dateOfJourney = request.POST['dateOfJourney']
        phoneNumber = request.POST['phoneNumber']
        pickUpAddress = request.POST['pickUpAddress']
        dropAddress = request.POST['dropAddress']
        complaintRegarding = request.POST['complaintRegarding']
        if request.POST['other']:
            other = request.POST['other']
            complaintRegarding = complaintRegarding + '-----' + other
        description = request.POST['description']

        form = ComplaintForm(userName = userName, 
                             dateOfJourney = dateOfJourney, 
                             phoneNumber = phoneNumber,
                             pickUpAddress = pickUpAddress,
                             dropAddress = dropAddress,
                             complaintRegarding = complaintRegarding,
                             description = description
                             )
        
        try: 
            form.save()
        except:
            print("Something Went Wrong.....") 
    else:
        print("Something Went Wrong Here also......")
        
    return render(request, 'user/complaintForm.html')
