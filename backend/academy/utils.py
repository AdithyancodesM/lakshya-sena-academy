import requests
import os

def send_enquiry_email(name, phone, message):
    api_key = os.environ.get("SENDGRID_API_KEY")
    if not api_key:
        return

    url = "https://api.sendgrid.com/v3/mail/send"

    payload = {
        "personalizations": [{
            "to": [{"email": "lakshyasenaacademy@gmail.com"}],
            "subject": "New Enquiry – Lakshya Sena Academy"
        }],
        "from": {"email": "lakshyasenaacademy@gmail.com"},
        "content": [{
            "type": "text/plain",
            "value": f"""
New enquiry received:

Name: {name}
Phone: {phone}
Message: {message}
"""
        }]
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        print("SendGrid status:", response.status_code)
        print("SendGrid response:", response.text)

    except Exception:
        pass
