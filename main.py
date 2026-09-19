import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_email(email):
    analysis = client.responses.create(
        model="gpt-5.5",
        input=email,
        instructions="""
        Analyze the given email.
        
        Return a JSON object with exactly these fields:
        
        - category: one of work, education, personal, finance, marketing, career, other
        - summary: a concise 1-2 sentence summary
        - priority: one of high, medium, low
        - suggested_action: one of reply, attend, review, pay, complete, ignore, save, schedule, other
        
        Return exactly a single option for category, priority, and suggested action.
        """
    )
    return analysis.output_text.strip()


email = """
Subject: Interview scheduled for Monday

Hi,

Thank you for applying for the AI Engineering Internship.
We would like to invite you to an interview on Monday at 10:00 AM.

Please confirm your availability.

Best,
ABC Technologies
"""

output = analyze_email(email)
print(output)