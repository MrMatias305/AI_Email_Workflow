import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AnalyzeEmail(BaseModel):
    category: str
    summary: str
    priority: str
    action: str


def analyze_email(email):
    response = client.responses.parse(
        model="gpt-5.5",
        input=f"""
        You are an AI email analysis assistant.
        
        Analyze the email and produce a structured assessment
        that helps the recipient understand what the email means
        and what they should do next.
        
        Follow these rules:
        
        1. CATEGORY
        Classify the email into exactly one of these categories:
        - work: workplace communication, tasks, meetings, or colleagues
        - education: university, school, courses, assignments, or academic matters
        - personal: messages from friends, family, or other personal contacts
        - finance: banking, payments, invoices, bills, or financial services
        - marketing: advertisements, promotions, newsletters, or sales offers
        - career: job applications, interviews, recruiters, internships, or career opportunities
        - other: anything that does not fit the categories above
        
        2. SUMMARY
        Summarize the email in 1-2 concise sentences.
        Capture the main purpose of the email and any important
        details such as dates, deadlines, amounts, or requests.
        Do not include unnecessary information.
        
        3. PRIORITY
        Determine how urgently the recipient needs to pay attention
        to the email:
        - high: requires immediate or time-sensitive attention, has an upcoming deadline,
          or could have significant consequences if ignored
        - medium: important and may require action, but is not immediately urgent
        - low: informational, optional, non-urgent, or promotional
        
        4. SUGGESTED ACTION
        Identify the most appropriate next action for the recipient.
        Choose the action based on what the email actually asks or implies.
        
        Available actions:
        - reply: respond to the sender
        - attend: attend a meeting, interview, event, or appointment
        - review: read or examine information
        - pay: make a payment
        - complete: complete a requested task
        - ignore: no action is necessary
        - save: keep the email for future reference
        - schedule: add something to a calendar or schedule
        - other: an action that does not fit the options above
        
        IMPORTANT:
        - Base your analysis only on the information contained in the email.
        - Do not invent missing details.
        - If the email does not require action, use an appropriate non-action option.
        - Consider deadlines and explicit requests when determining priority.
        - Return the result using the provided EmailAnalysis structure.
        
        Email: {email}
        """,
        text_format=AnalyzeEmail
    )
    return response.output_parsed


email = """
Subject: Interview scheduled for Monday

Hi,

Thank you for applying for the AI Engineering Internship.
We would like to invite you to an interview on Monday at 10:00 AM.

Please confirm your availability.

Best,
ABC Technologies
"""

result = analyze_email(email)

print("Category: ", result.category)
print("Summary: ", result.summary)
print("Priority: ", result.priority)
print("Action: ", result.action)