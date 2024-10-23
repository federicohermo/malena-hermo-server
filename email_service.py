from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Credentials for Gmail API
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

# Function to send an email using Gmail API
def send_email(sender: str, subject: str, message: str):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    email_msg = message
    mime_msg = MIMEMultipart()
    mime_msg['to'] = 'malehermo@gmail.com'
    mime_msg['subject'] = subject
    mime_msg.attach(MIMEText(email_msg, 'plain'))

    # Base64 encode the email message
    raw_string = base64.urlsafe_b64encode(mime_msg.as_bytes()).decode()

    # Send the email using Gmail API
    service.users().messages().send(userId='me', body={'raw': raw_string}).execute()