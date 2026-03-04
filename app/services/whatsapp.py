import requests

def send_message(phone, text):
    payload = {
        "to": phone,
        "message": text
    }

    requests.post("WHATSAPP_API_URL", json=payload)