# WhatsApp Chatbot using FastAPI

This project is a WhatsApp chatbot built using FastAPI and the Meta WhatsApp Cloud API.

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

   - GET /webhook?hub.mode=subscribe&hub.challenge=123456&hub.verify_token=abc

2. Receive WhatsApp Messages (POST)

   - POST /webhook

Logs incoming messages and sends an automated response.
