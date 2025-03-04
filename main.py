from fastapi import FastAPI, Request, Query
import requests
import json

app = FastAPI()

PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
VERIFY_TOKEN = "YOUR_VERIFY_TOKEN"
WHATSAPP_API_URL = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

DOCUMENTS = {
    "brochure": "https://www.example.com/brochure.pdf",
    "pricing": "https://www.example.com/pricing.pdf",
    "catalog": "https://www.example.com/catalog.pdf"
}

@app.get("/webhook")
def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge) 
    return {"status": "Verification failed"}

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.json()
    print("Received Data:", json.dumps(data, indent=2))

    changes = data.get("entry", [{}])[0].get("changes", [{}])[0].get("value", {})
    if "messages" in changes:
        message = changes["messages"][0]
        sender = message["from"]
        text = message.get("text", {}).get("body", "").strip().lower()

        if text in DOCUMENTS:
            send_whatsapp_message(sender, document_url=DOCUMENTS[text], document_caption=f"Here is your requested {text}")
        else:
            reply_text = process_message(text)
            send_whatsapp_message(sender, text=reply_text)

    return {"status": "received"}

def send_whatsapp_message(to, text=None, document_url=None, document_caption=None):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    if text:
        text_payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": text}
        }
        text_response = requests.post(WHATSAPP_API_URL, json=text_payload, headers=headers)
        print("Text Response:", text_response.json())

    if document_url:
        document_payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "document",
            "document": {
                "link": document_url, 
                "caption": document_caption 
            }
        }
        doc_response = requests.post(WHATSAPP_API_URL, json=document_payload, headers=headers)
        print("Document Response:", doc_response.json())

def process_message(text):
    if text == "hi":
        return "Hello! How can I assist you?"
    elif text == "bye":
        return "Goodbye! Have a great day!"
    else:
        return f"You said: {text}"

@app.get("/test-message/")
def test_message(to: str, text: str):
    if text.lower() in DOCUMENTS:
        send_whatsapp_message(to, document_url=DOCUMENTS[text.lower()], document_caption=f"Here is your requested {text}")
    else:
        reply_text = process_message(text)
        send_whatsapp_message(to, text=reply_text)
    return {"status": "Test message sent"}
