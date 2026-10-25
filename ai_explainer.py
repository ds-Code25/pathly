
import json
from google import genai
from google.genai import types


def generate_roadmap(
    interests,
    experience_level,
    career_goal,
    courses,
    projects,
    careers,
    api_key
):
    # Organize the student's information
    student_data = {
        "interests": interests,
        "experience_level": experience_level,
        "career_goal": career_goal,
        "courses": courses,
        "projects": projects,
        "careers": careers
    }

    # Connect to Gemini
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
            timeout=15000,
            retry_options=types.HttpRetryOptions(attempts=1)
        )
    )

    # Instructions for generating the roadmap
    
    prompt = f"""
    You are Pathly's AI career guidance assistant.

    Your task is to create a personalized career roadmap
    based on the student's background and Pathly's existing
    recommendations.

    STUDENT INFORMATION:
    {json.dumps(student_data, indent=2)}

    OUTPUT FORMAT:
    Create exactly 3 steps.

    For each step, provide:
    1. A clear step title.
    2. One useful skill to develop.
    3. One practical learning activity or project.
    4. A short explanation of why this step helps.

    RULES:
    - Adapt the difficulty to the student's experience level.
    - For beginners, start with foundational skills.
    - Make each step build logically on the previous one.
    - Ground recommendations in Pathly's supplied data.
    - Only name specific courses if they appear in the
    provided courses list.
    - Do not generate URLs, even for suggested courses.
    - You may suggest general project ideas, but distinguish
    them from projects already recommended by Pathly.
    - Do not guarantee career or employment outcomes.
    - Acknowledge missing information when relevant.
    - Keep the roadmap concise, around 200 words.
    - Do not introduce yourself.
    """


    # Send the prompt to Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    # Return the generated roadmap
    return response.text
