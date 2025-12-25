import re
import urllib.parse

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .models import Enquiry


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
            # ✅ Save to database
            Enquiry.objects.create(
                name=name,
                phone=phone,
                message=message
            )

            # ✅ Email notification (fails silently in production)
            try:
                send_mail(
                    subject="New Enquiry – Lakshya Sena Academy",
                    message=f"""
New enquiry received:

Name: {name}
Phone: {phone}
Message: {message}
""",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass

            # ✅ WhatsApp notification URL (admin use)
            message_text = f"New enquiry:\nName: {name}\nPhone: {phone}"
            encoded = urllib.parse.quote(message_text)
            whatsapp_url = f"https://wa.me/919380502805?text={encoded}"

            success = True

    return render(request, "contact.html", {
        "success": success,
        "error": error
    })


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')
