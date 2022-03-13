from itertools import dropwhile
import re
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

from aicteapp.models import EventRegistration
from participantapp.models import ParticipantGeneralDetails

# Create your views here.
def participantdb(request):
    return render(request, 'participantapp/participantdb.html')

def participantlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('participantdb')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('participantlogin')
    else: 
        return render(request,'participantapp/login.html')

def participantcreateaccount(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('home')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('home')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                return redirect('participantlogin')

    return render(request,'participantapp/register.html')

def participantevent(request):
    eventlist = EventRegistration.objects.all()
    return render(request,'participantapp/participantevent.html',{'eventlist':eventlist})

def participanteventregistration(request,pk):
    eventlist = EventRegistration.objects.get(id = pk)
    if request.method == 'POST':
        id = eventlist.id
        username = request.POST['username']
        eventname = request.POST['eventname']
        eventid =request.POST['eventid']
        phoneno =request.POST['phoneno']
        email = request.POST['email']
        dob = request.POST['dob']
        city = request.POST['city']
        address = request.POST['address']
        state = request.POST['state']
        alternameemail = request.POST['alternateemail']
        whatsappnumber = request.POST['whatsappnumber']

        participantgeneraldetails = ParticipantGeneralDetails(id=id,username=username,phoneno=phoneno,eventname=eventname,eventid= eventid ,email=email,dob=dob,city=city,address=address,state=state,alternameemail=alternameemail,whatsappnumber=whatsappnumber)
        participantgeneraldetails.save()
    return render(request,'participantapp/registeration.html',{'eventlist':eventlist})

def participantgeneraldetails(request):
    return render(request,'participantapp/participantgeneraldetails.html')

def participantlogout(request):
    auth.logout(request)
    return redirect('participantdb')