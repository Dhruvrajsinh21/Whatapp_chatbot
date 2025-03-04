## Branches 

- **`main`** - WhatsApp chatbot built using FastAPI.
- **`Documentation_WhatsappAPIs`** - Documented the WhatsApp Cloud APIs(Meta APIs).

# WhatsApp Chatbot using FastAPI

This project is a demo of WhatsApp chatbot built using custom method using FastAPI and the Meta WhatsApp Cloud API.
- Video link (setup): https://drive.google.com/file/d/1i6QioH2OdlWg29xF7z-sNLXl2mFKkqP-/view?usp=sharing
- Video link (conversation): https://drive.google.com/file/d/10ijkYXhgWzQLeYPMHTIU_ZG2q95Egb_9/view?usp=sharing

## Setup Instructions

1. Install Dependencies
```bash
pip install fastapi uvicorn requests
```

2. Start FastAPI Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

3. Setup Ngrok (For Public URL)
```bash
ngrok http 8000
#Copy the https://... URL and update it in the Meta Developer Console.
```

4. Configure Webhook in Meta Console

   - Go to Meta Developer Console.

   - Navigate to WhatsApp > Configuration.

   - Set Webhook URL to: https://<YOUR_NGROK_URL>/webhook.

   - Subscribe to the messages event.

5. Verify Webhook (GET Request)

   - Meta will call /webhook for verification. Ensure VERIFY_TOKEN in main.py matches the one set in Meta.

## API Endpoints

1. Verify Webhook
```bash
   GET /webhook?hub.mode=subscribe&hub.challenge=123456&hub.verify_token=abc
```
2. Receive WhatsApp Messages (POST)
```bash
   POST /webhook
```
Logs incoming messages and sends an automated response.
