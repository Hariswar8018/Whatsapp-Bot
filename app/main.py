from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

AUTOMATEAI_TOKEN = "R2uDvAAGG66Y9klGF790Hnaluu0Me31CjLO5PB89"
BASE_URL = "https://live.theautomate.ai"

@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    print("Incoming:", data)

    phone = data.get("phone")
    message = data.get("message")

    if message == "hi":
        send_buttons(phone)

    return {"status": "ok"}

def send_buttons(phone):

    url = f"{BASE_URL}/api/send"

    headers = {
        "Authorization": f"Bearer {AUTOMATEAI_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "phone": phone,
        "message": "Welcome Ayusman's Bot 🤖",
        "header": "Choose an option",
        "footer": "AI Engineering Bot",
        "buttons": [
            {
                "id": "btn_1",
                "title": "Check Facts"
            },
            {
                "id": "btn_2",
                "title": "More Info"
            }
        ]
    }

    requests.post(url, headers=headers, json=payload)