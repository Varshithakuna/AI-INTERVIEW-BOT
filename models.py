from dataclasses import dataclass, field


@dataclass
class Candidate:

    # ==========================
    # Candidate Details
    # ==========================

    name: str
    role: str
    experience: str

    resume_text: str = ""

    # ==========================
    # Interview Configuration
    # ==========================

    interview_type: str = "Technical"

    difficulty: str = "Medium"

    total_questions: int = 10

    interview_mode: str = "💬 Chat"

    # ==========================
    # Runtime
    # ==========================

    history: list = field(default_factory=list)

    interview_complete: bool = False

    current_question: int = 0