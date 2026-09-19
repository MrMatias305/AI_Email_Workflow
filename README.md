# AI Email Workflow

An AI-powered email workflow that connects to Gmail, analyzes real emails, and turns them into concise, actionable information.

This project demonstrates practical AI automation, structured AI outputs, workflow logic, Gmail API integration, and modular Python architecture.

## Current Workflow

```text
Gmail
  ↓
Fetch email
  ↓
Extract sender / subject / body
  ↓
AI analysis
  ├── Category
  ├── Summary
  ├── Priority
  └── Suggested action
  ↓
Deterministic workflow rules
  ↓
Final result
```

## Features

* Connects to Gmail using the Gmail API
* Authenticates with Google OAuth 2.0
* Retrieves real Gmail messages
* Extracts:

  * Sender
  * Subject
  * Email body
* Classifies emails into categories
* Generates concise summaries
* Detects email priority
* Suggests an appropriate action
* Produces structured AI output using Pydantic
* Applies deterministic workflow rules after AI analysis
* Separates Gmail integration, AI workflow logic, and data models into different modules

## AI Analysis

Each email is analyzed using four main dimensions.

### Category

Emails are classified as:

* `work`
* `education`
* `personal`
* `finance`
* `marketing`
* `career`
* `other`

### Summary

The system generates a concise 1–2 sentence summary containing the important purpose, requests, deadlines, dates, or amounts when relevant.

### Priority

Emails are assigned one of three priority levels:

* `high` — immediate or time-sensitive attention may be required
* `medium` — important, but not immediately urgent
* `low` — informational, optional, or non-urgent

### Suggested Action

The system can suggest actions such as:

* `reply`
* `attend`
* `review`
* `pay`
* `complete`
* `ignore`
* `save`
* `schedule`
* `other`

## Workflow Logic

The AI analysis is followed by deterministic Python rules.

For example:

```text
High priority
    → needs_attention

Ignore action
    → no_action

Everything else
    → normal
```

This keeps the AI responsible for understanding the email while normal Python logic controls the application's workflow behavior.

## Project Structure

```text
AI_Email_Workflow/
├── main.py
├── workflow.py
├── models.py
├── gmail.py
├── README.md
├── .env
├── credentials.json
├── token.json
├── .gitignore
└── .venv/
```

### `main.py`

Application entry point.

Responsible for:

* Connecting to Gmail
* Retrieving an email
* Passing the email into the workflow
* Displaying the analysis and workflow result

### `gmail.py`

Gmail integration layer.

Responsible for:

* Google OAuth authentication
* Creating the Gmail API service
* Retrieving Gmail messages
* Extracting sender, subject, and body

### `workflow.py`

AI and workflow layer.

Responsible for:

* Sending email content to the AI model
* Generating structured analysis
* Applying deterministic workflow rules

### `models.py`

Defines the structured AI output using Pydantic.

```python
class EmailAnalysis(BaseModel):
    category: str
    summary: str
    priority: str
    suggested_action: str
```

## Technologies

* Python
* OpenAI API
* Pydantic
* Gmail API
* Google OAuth 2.0
* `google-api-python-client`
* `google-auth-oauthlib`

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/MrMatias305/AI_Email_Workflow.git
cd AI_Email_Workflow
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install openai pydantic google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 4. Configure OpenAI

Create a `.env` file containing your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`.

### 5. Configure Gmail API

Create a Google Cloud project and enable the Gmail API.

Create OAuth 2.0 Desktop App credentials and place the downloaded credentials file in the project directory as:

```text
credentials.json
```

On the first run, Google OAuth authenticates the account and generates:

```text
token.json
```

Both files contain sensitive credentials and must remain local.

## Running the Project

Run:

```bash
python main.py
```

The application retrieves a real Gmail message and produces an analysis such as:

```text
========== EMAIL ==========
From: someone@example.com
Subject: Assignment submission

========== AI ANALYSIS ==========
Category: education
Summary: The email contains information about an upcoming assignment deadline.
Priority: high
Suggested Action: complete

========== WORKFLOW ==========
Status: needs_attention
```

The exact result depends on the email being analyzed.

## Security

Sensitive credentials should never be committed to Git.

The following files should be ignored:

```text
.env
credentials.json
token.json
.venv/
venv/
__pycache__/
```

## Design Principles

### AI for Understanding

The AI handles tasks that require natural-language understanding:

* Classification
* Summarization
* Priority interpretation
* Action suggestion

### Python for Control

Deterministic Python logic handles workflow decisions that should remain predictable.

### Separation of Concerns

Each module has a focused responsibility:

```text
Gmail integration → gmail.py
AI + workflow     → workflow.py
Data structures   → models.py
Application entry → main.py
```

This makes the project easier to test, extend, and maintain.

## Current Scope

The current version focuses on a simple read-only workflow:

```text
READ → ANALYZE → REPORT
```

It does not automatically:

* Send emails
* Reply to emails
* Delete emails
* Modify Gmail messages
* Change labels

## Learning Outcomes

This project was built to practice:

* AI-assisted software development
* Prompt engineering
* Structured LLM outputs
* AI workflow design
* API integration
* OAuth authentication
* Python modular architecture
* Deterministic automation rules
* Real-world AI productivity applications

## Project Status

**Working prototype**

The system can successfully retrieve a real Gmail email, analyze it with AI, and return a concise structured workflow result.
