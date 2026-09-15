import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_URL = "http://127.0.0.1:5000"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def get_college_data():
    response = requests.get(f"{API_URL}/college")

    if response.status_code == 200:
        return response.json()

    return None


def get_syllabus_data(semester):

    response = requests.get(
        f"{API_URL}/syllabus/{semester}"
    )

    if response.status_code == 200:
        return response.json()

    return None


def ask_ai(question, context):

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=f"""
You are CollegeMate AI, a helpful assistant for diploma CSE students.

Use the provided project data as the main source of information.

Project Data:
{context}

Student Question:
{question}

Give a simple, clear and useful answer.

If the requested information is not available
in the provided project data, clearly say so.
"""
    )

    return response.output_text


def college_ai(question):

    context = get_college_data()

    if context is None:
        return "College data could not be loaded."

    return ask_ai(question, context)


def study_ai(question, semester):

    context = get_syllabus_data(semester)

    if context is None:
        return "Syllabus data could not be loaded."

    return ask_ai(question, context)