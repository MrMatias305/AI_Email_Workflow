from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

email = """
Subject: Interview scheduled for Monday

Hi,

Thank you for applying for the AI Engineering Internship.
We would like to invite you to an interview on Monday at 10:00 AM.

Please confirm your availability.

Best,
ABC Technologies
"""

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

print("Category:", response.output_text)