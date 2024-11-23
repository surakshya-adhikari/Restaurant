from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact  # Assuming you have a Contact model
from django.conf import settings
from datetime import datetime

date=datetime.now()
# Create your views here.
def index(request):
    return render(request, 'main/index.html',{'date':date})

def about(request):
    return render(request, 'main/about.html',{'date':date})

def services(request):
    return render(request, 'main/services.html')

def menu(request):
    return render(request, 'main/menu.html')

''' Authentication part'''
def register(request):
    return render(request,'auth/register.html')

# def contact(request):
#     if request.method == 'POST':
#         # Get form data from POST request
#         name = request.POST.get('name')
#         email = request.POST.get('email')  # This will be the dynamic recipient
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')

#         # Create an email subject and body
#         subject = f'New Contact Form Submission from {name}'
#         message_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'

#         # Email sending configuration
#         try:
#             send_mail(
#                 subject,
#                 message_body,
#                 settings.EMAIL_HOST_USER,  # Sender email from settings
#                 [email],  # Dynamic recipient email from the form
#                 fail_silently=False,
#             )

#             # Optionally, save the contact information to the database
#             Contact.objects.create(name=name, email=email, phone=phone, message=message)

#             return redirect('success_page')  # Redirect to a success page
#         except Exception as e:
#             print(f"Error sending email: {e}")
#             return render(request, 'main/contact.html', {'error': 'There was an error sending the email.'})

#     return render(request, 'main/contact.html')
