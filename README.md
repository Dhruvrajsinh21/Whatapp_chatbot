# WhatsApp Business API Endpoints

## Official Postman Collection link (referred):
https://gold-trinity-812977.postman.co/workspace/My-Workspace~b4dd7082-bed7-4e30-8609-aec9a65ac7fd/collection/34688781-70103586-a21a-4d14-807c-a6124dedaeb7?action=share&creator=34688781

## 1. **Phone Number Information**
**Endpoint:**  
```
GET https://graph.facebook.com/v18.0/<PHONE_NUMBER_ID>
```
**Purpose:**  
- Retrieves details about the registered phone number, including its display name and verification status.  

**Response Example:**  
```json
{
  "id": "PHONE_NUMBER_ID",
  "display_phone_number": "+1234567890",
  "verified_name": "Your Business Name"
}
```

---

## 2. **Send a Message**
**Endpoint:**  
```
POST https://graph.facebook.com/v18.0/<PHONE_NUMBER_ID>/messages
```
**Purpose:**  
- Sends text, images, videos, or template messages to users.  

**Request Example (Text Message):**  
```json
{
  "messaging_product": "whatsapp",
  "to": "+1234567890",
  "type": "text",
  "text": { "body": "Hello! This is an automated response." }
}
```

**Response Example:**  
```json
{
  "messages": [{ "id": "wamid.123456" }]
}
```

---

## 3. **Send a Template Message**  
**Request Example:**  
```json
{
  "messaging_product": "whatsapp",
  "to": "+1234567890",
  "type": "template",
  "template": {
    "name": "order_confirmation",
    "language": { "code": "en_US" },
    "components": [{
      "type": "body",
      "parameters": [{ "type": "text", "text": "Order #12345" }]
    }]
  }
}
```

---

## 4. **Manage Message Templates**
**Endpoint (List Templates):**  
```
GET https://graph.facebook.com/v18.0/<WHATSAPP_BUSINESS_ACCOUNT_ID>/message_templates
```
**Purpose:**  
- Fetches all pre-approved message templates.  

**Response Example:**  
```json
{
  "data": [
    {
      "name": "order_confirmation",
      "status": "APPROVED",
      "language": "en_US"
    }
  ]
}
```

---

## 5. **Upload and Manage Media**
**Endpoint (Upload Media):**  
```
POST https://graph.facebook.com/v18.0/<PHONE_NUMBER_ID>/media
```
**Purpose:**  
- Uploads media files (images, videos, documents) for use in messages.  

**Request Example:**  
```json
{
  "file": "https://yourdomain.com/image.jpg",
  "type": "image/jpeg"
}
```

**Response Example:**  
```json
{
  "id": "MEDIA_ID"
}
```

**Endpoint (Retrieve Media Info):**  
```
GET https://graph.facebook.com/v18.0/<MEDIA_ID>
```

---

## 6. **Get Message Status**
**Endpoint:**  
```
GET https://graph.facebook.com/v18.0/<MESSAGE_ID>
```
**Purpose:**  
- Checks the delivery status of a sent message.  

**Response Example:**  
```json
{
  "id": "MESSAGE_ID",
  "status": "delivered"
}
```

---

## 7. **Manage WhatsApp Business Profile**
**Endpoint (Update Profile):**  
```
POST https://graph.facebook.com/v18.0/<PHONE_NUMBER_ID>/settings
```
**Purpose:**  
- Updates the business profile (name, description, etc.).  

**Request Example:**  
```json
{
  "about": "We provide the best customer service."
}
```

