from llm import ask_llm
from memory import ConversationMemory
from prompts import SYSTEM_PROMPT
from evaluation import generate_evaluation


class InterviewAgent:

    def __init__(self, candidate):

        self.candidate = candidate
        self.memory = ConversationMemory()
        self.finished = False

        # Store system prompt
        self.memory.add(
            "system",
            SYSTEM_PROMPT
        )

    # ---------------------------------------
    # Start Interview
    # ---------------------------------------
    def start_interview(self):

        prompt = f"""
You are conducting a professional interview.

Candidate Details

Name:
{self.candidate.name}

Role:
{self.candidate.role}

Experience:
{self.candidate.experience}

Resume:

{self.candidate.resume_text}

Instructions:

1. Carefully analyze the resume.
2. Identify projects, internships, certifications and technical skills.
3. If a resume exists, start by asking resume-based questions.
4. Otherwise begin with a professional introduction.
5. Ask ONLY ONE interview question at a time.
6. Never answer your own question.
7. Behave like an experienced interviewer.
8. Keep the interview conversational.
9. Remember previous answers and ask relevant follow-up questions.
"""

        self.memory.add(
            "user",
            prompt
        )

        reply = ask_llm(
            self.memory.get_history()
        )

        self.memory.add(
            "assistant",
            reply
        )

        return reply

    # ---------------------------------------
    # Continue Interview
    # ---------------------------------------
    def process_answer(self, answer):

        self.memory.add(
            "user",
            answer
        )

        reply = ask_llm(
            self.memory.get_history()
        )

        self.memory.add(
            "assistant",
            reply
        )

        return reply

    # ---------------------------------------
    # Generate Final Evaluation
    # ---------------------------------------
    def generate_report(self):

        history = ""

        for message in self.memory.get_history():

            role = message["role"].upper()
            content = message["content"]

            history += f"{role}: {content}\n\n"

        return generate_evaluation(history)