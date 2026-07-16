class CandidateSession:

    def __init__(self):

        # ==========================
        # Candidate Details
        # ==========================

        self.name = ""
        self.role = ""
        self.experience = ""

        self.resume = None
        self.resume_text = ""

        # ==========================
        # Interview Configuration
        # ==========================

        self.interview_type = "Technical"
        self.difficulty = "Medium"
        self.total_questions = 10
        self.interview_mode = "💬 Chat"

        # ==========================
        # Runtime
        # ==========================

        self.interview_started = False
        self.interviewer = None

        # ==========================
        # Interview History
        # ==========================

        self.interview_history = []

        # ==========================
        # Current Report
        # ==========================

        self.current_report = None