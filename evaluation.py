import json

from llm import ask_llm


def generate_evaluation(history):

    prompt = f"""
You are an expert software engineering interviewer.

Below is the complete interview conversation.

{history}

Evaluate the candidate objectively.

Return ONLY valid JSON.

Do not return markdown.
Do not return explanations.
Do not use ```json.

Return this exact JSON format:

{{
    "candidate_name": "",
    "role": "",
    "questions_answered": 0,
    "technical_score": 0,
    "communication_score": 0,
    "problem_solving_score": 0,
    "confidence_score": 0,
    "overall_score": 0,
    "strengths": [],
    "weaknesses": [],
    "suggestions": [],
    "recommendation": ""
}}

Rules:

- Technical score: 0-10
- Communication score: 0-10
- Problem solving: 0-10
- Confidence: 0-10
- Overall score: 0-100
- Return ONLY JSON.
"""

    response = ask_llm([
        {
            "role": "user",
            "content": prompt
        }
    ])

    try:
        return json.loads(response)

    except Exception:
        return {
            "error": "AI returned invalid JSON.",
            "raw_response": response
        }