import re
from django.shortcuts import render
from .models import Enquiry
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
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        pattern = re.compile(r'^(?:\+91)?[6-9]\d{9}$')

        if not pattern.match(phone):
            error = "Please enter a valid Indian mobile number."
        else:
            # ✅ SAVE TO DATABASE (SAFE)
            Enquiry.objects.create(
                name=name,
                phone=phone,
                message=message
            )

            # ❌ DO NOT SEND EMAIL HERE (PRODUCTION SAFE)
            success = True

    return render(request, "contact.html", {
        "success": success,
        "error": error
    })


def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')
