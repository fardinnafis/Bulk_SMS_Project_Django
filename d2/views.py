from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from d2.models import AddPeople
from d2.models import ErrorMessage, Feedback
from django.contrib import messages
from django.shortcuts import redirect
from d2.forms import FeedbackForm
from django.urls import reverse
from django.http import JsonResponse
import requests
import random
from django.contrib.auth.forms import UserCreationForm
from d2.forms import SignupForm
# Define API key error codes
api_key_messages = {
    "Message Sent successfully": "445000",
    "missing api key": "445010",
    "missing contact number": "445020",
    "missing sender id": "445030",
    "Invalid api key": "445040",
    "Your account was suspended": "445050",
    "Your account was expired": "445060",
    "Only a user can send sms": "445070",
    "Invalid sender id": "445080",
    "You have no access to this sender id": "445090",
    "All numbers are invalid": "445110",
    "insufficient balance": "445120",
    "reseller insufficient balance": "445130",
    "You are not a user": "445170"
}

def home(request):
    if request.method == "POST":
        # Get form data
        number = request.POST.get('phone')
        senderID = request.POST.get('ID')
        sms = request.POST.get('sms')
        textCode = request.POST.get('text')
        gg="Success to send SMS"
        # Check if required fields are missing
        if not textCode:
            gg = "missing api key"
            error = ErrorMessage(code=api_key_messages[gg], message=f"missing api key")
            error.save()
            messages.error(request, f"missing api key, Code: {api_key_messages[gg]} ")

            return redirect('home')

        if not number:
            gg = "missing contact number"
            error = ErrorMessage(code=api_key_messages[gg], message=f"missing contact number")
            error.save()
            messages.error(request, f"missing contact number, Code: {api_key_messages[gg]} ")
            return redirect('home')

        if not senderID:
            gg = "Invalid sender id"
            error = ErrorMessage(code=api_key_messages[gg], message=f"Invalid sender id")
            error.save()
            messages.error(request, f"Invalid sender id, Code: {api_key_messages[gg]} ")
            return redirect('home')
        
        if not sms:
            gg = "Invalid sms"
            error = ErrorMessage(code=api_key_messages[gg], message=f"Invalid sms")
            error.save()
            messages.error(request, f"Invalid sms, Code: {api_key_messages[gg]} ")
            return redirect('home')
        
        # Construct URL and make API call
        otp = random.randint(1000, 9999)
        url = f'http://sms.iglweb.com/api/v1/send?api_key={textCode}&contacts={number}&senderid={senderID}&msg={sms}'
        response = requests.get(url)
        
        # Check API response for errors
        if response.status_code == 200:
            values = AddPeople(number=number, senderID=senderID, sms=gg, textCode=textCode)
            values.save()
            messages.success(request, f"Success to send SMS")
            return redirect('home')
        else:
            gg = "No message has been sent"
            messages.error(request, f"{gg}, Code: {response.status_code}")
            return redirect('home')
    else:
        return render(request, 'test.html')


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
            
       
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})