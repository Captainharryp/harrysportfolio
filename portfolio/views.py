from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact, Subscribe
from django.core.mail import send_mail

def index(request):
	return render(request,'index.html', {})

def about(request):
	return render(request,'about.html', {})

def portfolio(request):
	return render(request,'portfolio.html', {})

def services(request):
	return render(request,'services.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create and save a new Contact object
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send an email
        send_mail(
            subject,
            message,
            email,  # Your 'from_email' should go here
            ['abcaptain60@gmail.com'],  # Put recipient email addresses in a list
            fail_silently=False,  # Set this to True if you don't want to raise exceptions on errors
        )

        alert_title = "Form Submitted!"
        alert_message = "I am happy to hear from you. I will get back to you as soon as possible."

        return render(request, 'contact.html', {'name': name, 'alert_title': alert_title, 'alert_message': alert_message})

    else:
        return render(request, 'contact.html', {})




def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # Create a new Subscribe object and save it to the database
        new_subscription = Subscribe.objects.create(email=email)

        # Send a confirmation email to the subscriber (optional)
        send_mail(
            "Subscription Confirmation",
            "Thank you for subscribing!",
            [email], # Send the confirmation email to the subscriber
            ['abcaptain60@gmail.com'],  
            fail_silently=False,  # Set this to True if you don't want to raise exceptions on errors
        )

        # Return a JSON response indicating success
        return JsonResponse({'success': True, 'message': 'Subscription successful!'})
    else:
        # Handle GET requests or any other method as needed
        return render(request, 'index.html')
