from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # You can create a success page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def about(request):
    return render(request, 'about.html')


from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('index')  # Or redirect to 'contact' with a thank-you message

    return render(request, 'contact.html')
def books(request):
    return render(request, 'book_by_category.html')

def books_by_author(request):
    return render(request, 'books_by_author.html')
def token(request):
    consumer_key = 'ZM5qF2qg1xyINYFL5d2GbLbTaASz7GJJAb2jEvie7KMHPqaD'
    consumer_secret = 'BHmsoqw48U6pzcLiEyJxYuiQUfanVJ8aTuj4x6Lfxuu3wYZS83emDGDmxNbAXxIS'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})
def pay(request):
    if request.method == 'POST':
        book = request.POST.get('book_title')
        amount = request.POST.get('amount')
        phone = request.POST.get('phone_number')

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json"
        }

        payload = {
            "BusinessShortCode": "174379",
            "Password": "YOUR_ENCODED_PASSWORD",
            "Timestamp": "YOUR_TIMESTAMP",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://yourdomain.com/callback/",
            "AccountReference": book,
            "TransactionDesc": "Book Purchase"
        }

        response = requests.post(api_url, json=payload, headers=headers)
        return render(request, 'index.html', {'response': response.json()})

    return render(request, 'pay.html')
def stk(request):
    return render(request, 'pay.html', {'navbar': 'stk'})
