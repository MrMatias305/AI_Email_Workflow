import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Classify email into a category
# e.g., work, education, personal...
def classify_email(email):
    response = client.responses.create(
        model='gpt-5.5',
        input=email,
        instructions="""
        Classify the email into exactly one category.

        Available categories:
        - work
        - education
        - personal
        - finance
        - marketing
        - career
        - other

        Return only the category name.
        """
    )

    return response.output_text.strip()


# Summarize email
def summarize_email(email):
    response = client.responses.create(
        model='gpt-5.5',
        input=email,
        instructions="""
        Summarize the following email in 1-2 concise sentences.
        
        Focus on:
        - What the email is about
        - Any important information
        - Any action the recipient may need to take
        """
    )
    return response.output_text.strip()

# Set priority
def determine_priority(email):
    response = client.responses.create(
        model='gpt-5.5',
        input=email,
        instructions="""
        Determine the priority of this email.
        
        Choose exactly one:
        - high
        - medium
        - low
        
        Guidelines:
        - high: urgent, time-sensitive, or requires immediate action
        - medium: important but not immediately urgent
        - low: informational, optional, or promotional
        
        Return only the priority level.
        """
    )
    return response.output_text.strip()


email = """
Subject: Interview scheduled for Monday

Hi,

Thank you for applying for the AI Engineering Internship.
We would like to invite you to an interview on Monday at 10:00 AM.

Please confirm your availability.

Best,
ABC Technologies
"""

category = classify_email(email)
summary = summarize_email(email)
priority = determine_priority(email)

print("Category: ", category)
print("Summary: ", summary)
print("Priority: ", priority)