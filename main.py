from workflow import process_email

emails = [
    """
    Subject: Internship Interview

    We would like to invite you to an interview
    tomorrow at 10 AM. Please confirm your availability.
    """,

    """
    Subject: Assignment Deadline

    The deadline for your Enterprise Architecture
    assignment has been extended until next Friday.
    """,

    """
    Subject: Special Weekend Offer

    Get 40% off all shoes this weekend!
    Shop now before the offer ends.
    """
]


for index, email in enumerate(emails, start=1):
    result = process_email(email)
    analysis = result['analysis']

    print(f"\n--- EMAIL {index} ---")
    print("Category: ", analysis.category)
    print("Summary: ", analysis.summary)
    print("Priority: ", analysis.priority)
    print("Suggested Action: ", analysis.action)
    print("Status: ", result['status'])
