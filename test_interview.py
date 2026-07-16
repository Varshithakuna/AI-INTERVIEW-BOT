from interview_agent import InterviewAgent
from models import Candidate

candidate = Candidate(
    name="Varshitha",
    role="Python Developer",
    experience="Fresher"
)

agent = InterviewAgent(candidate)

print(agent.start_interview())

while True:
    answer = input("\nYou: ")

    response = agent.process_answer(answer)

    print("\nInterviewer:", response)