import re
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    success = False
    error = None

    if request.method == "POST":
        from .models import Enquiry  # safe import

        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        pattern = re.compile(r'^(?:\+91)?[6-9]\d{9}$')

        if not pattern.match(phone):
            error = "Please enter a valid Indian mobile number."
        else:
            # Save to DB
            Enquiry.objects.create(
                name=name,
                phone=phone,
                message=message
            )

            # Send email notification
            send_mail(
                subject='New Enquiry – Lakshya Sena Academy',
                message=f'''
New enquiry received:

Name: {name}
Phone: {phone}
Message: {message}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['lakshyasenaacademy@gmail.com'],
                fail_silently=False,
            )

            success = True

    return render(request, 'contact.html', {
        'success': success,
        'error': error
    })

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')
