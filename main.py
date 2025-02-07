from fastapi import FastAPI, Request, Query
import requests
import json

app = FastAPI()

# WhatsApp API Credentials (Replace with actual values)
PHONE_NUMBER_ID = "498746293331939"
ACCESS_TOKEN = "EAAJOI60HSKcBO8KS9WDeSDQykyfTSPUW8apZBePvKa6F5CHu2BnUdT2jCPTBJBtId4Nq63y5AFD9BpW26zFaOnhZAzJHYqO9n1ezmfrsiGrnN6wP9thBeySqZATkNwa7TTGUvkFUm1DRZATasZBUTwFXPY8aj62tWDHcTumyoGZAZAccvEy5D24JRIAn6KWyikJ8QCwiv5uxgNIZAwSwKxPb09JexZCSXEk8XF70ZD"
VERIFY_TOKEN = "abc"  # Choose any string
WHATSAPP_API_URL = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

# ✅ Step 1: Verify Webhook (Meta Calls This to Verify)
@app.get("/webhook")
def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)  # Meta requires integer response
    return {"status": "Verification failed"}

# ✅ Step 2: Receive Messages from WhatsApp
@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.json()
    print("Received Data:", json.dumps(data, indent=2))

    # ✅ Check if a message exists in the received data
    changes = data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {})
    if "messages" in changes:
        message = changes["messages"][0]  # Get first message
        sender = message["from"]
        text = message.get("text", {}).get("body", "")

        # ✅ Process the received message
        reply_text = process_message(text)
        send_whatsapp_message(sender, reply_text)

    return {"status": "received"}


# ✅ Step 3: Send WhatsApp Message
def send_whatsapp_message(to, text):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
    print(response.json())

# ✅ Step 4: Process Incoming Messages (Simple Reply)
def process_message(text):
    if text.lower() == "hi":
        return "Hello! How can I help you?"
    elif text.lower() == "bye":
        return "Goodbye! Have a great day!"
    else:
        return f"You said: {text}"
