from gmail import get_gmail_service, get_email, extract_message
from workflow import process_email

def main():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        maxResults=3
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')

    message_id = messages[2]['id']

    raw_message = get_email(service, message_id)
    email = extract_message(raw_message)

    result = process_email(f"""
        Sender: {email['sender']}
        Subject: {email['subject']}

        Body: {email['body']}
    """)

    analysis = result['analysis']

    print("Category: ", analysis.category)
    print("Summary: ", analysis.summary)
    print("Priority: ", analysis.priority)
    print("Suggested Action: ", analysis.action)
    print("Status: ", result['status'])


if __name__ == '__main__':
    main()

