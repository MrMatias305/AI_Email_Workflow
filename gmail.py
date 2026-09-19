import base64
import os

from google.auth.transport import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_gmail_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


def get_email(service, message_id):
    message = service.users().messages().get(
        userId='me',
        id=message_id,
        format='full'
    ).execute()

    return message


def extract_message(message):
    headers = message['payload'].get('headers', [])

    subject = ""
    sender = ""

    for header in headers:
        if header['name'].lower() == 'subject':
            subject = header['value']

        if header['name'].lower() == 'from':
            sender = header['value']

    body = ""

    payload = message['payload']

    if 'body' in payload and payload['body'].get('data'):
        data = payload['body']['data']
        body = base64.urlsafe_b64decode(data).decode('utf-8')

    elif 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body'].get('data')

                if data:
                    body = base64.urlsafe_b64decode(data).decode('utf-8')
                    break

    return {
        'id': message['id'],
        'sender': sender,
        'subject': subject,
        'body': body,
    }


if __name__ == '__main__':
    gmail_service = get_gmail_service()

    results = gmail_service.users().messages().list(
        userId='me',
        maxResults=3
    ).execute()

    messages = results.get('messages', [])

    if messages:
        message_id = messages[1]['id']
        message = get_email(gmail_service, message_id)
        email = extract_message(message)

        print("Sender: ", email['sender'])
        print("Subject: ", email['subject'])
        print("Body: ", email['body'])