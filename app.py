import streamlit as st

from session import CandidateSession
from models import Candidate
from interview_agent import InterviewAgent
from resume_parser import extract_resume_text
from database.interview_repository import save_interview

from ui.styles import load_css
from ui.hero import render_hero
from ui.home import render_home
from ui.interview import render_interview
from ui.evaluation import render_evaluation
from ui.history import render_history


# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="AI Interview Partner",
    page_icon="🎤",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)


# ==================================================
# Session State
# ==================================================

if "candidate" not in st.session_state:
    st.session_state.candidate = CandidateSession()

if "question" not in st.session_state:
    st.session_state.question = ""

if "report" not in st.session_state:
    st.session_state.report = None

if "interview_finished" not in st.session_state:
    st.session_state.interview_finished = False

candidate = st.session_state.candidate


# ==================================================
# Hero Section
# ==================================================

render_hero()


# ==================================================
# Home Screen
# ==================================================

if not candidate.interview_started:

    (
        candidate,
        interview_type,
        difficulty,
        total_questions,
        interview_mode
    ) = render_home(candidate)

    candidate.interview_type = interview_type
    candidate.difficulty = difficulty
    candidate.total_questions = total_questions
    candidate.interview_mode = interview_mode

    resume_text = ""

    if candidate.resume is not None:

        resume_text = extract_resume_text(candidate.resume)

        candidate.resume_text = resume_text

        st.success("✅ Resume uploaded successfully!")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🚀 Start AI Interview",
        use_container_width=True
    ):

        candidate_data = Candidate(

            name=candidate.name,

            role=candidate.role,

            experience=candidate.experience,

            resume_text=resume_text,

            interview_type=candidate.interview_type,

            difficulty=candidate.difficulty,

            total_questions=candidate.total_questions,

            interview_mode=candidate.interview_mode

        )

        candidate.interviewer = InterviewAgent(candidate_data)

        candidate.interview_started = True

        st.session_state.interview_finished = False
        st.session_state.report = None

        st.session_state.question = (
            candidate.interviewer.start_interview()
        )

        st.rerun()


# ==================================================
# Interview Screen
# ==================================================

if (
    candidate.interview_started
    and
    not st.session_state.interview_finished
):

    answer, submit, end = render_interview(
        st.session_state.question
    )

    if submit:

        if answer.strip():

            st.session_state.question = (
                candidate.interviewer.process_answer(
                    answer
                )
            )

            st.rerun()

    if end:

        with st.spinner(
            "Generating Interview Evaluation..."
        ):

            report = (
                candidate.interviewer.generate_report()
            )

            st.session_state.report = report

            candidate.current_report = report

            if (
                report is not None
                and isinstance(report, dict)
                and "error" not in report
            ):

                candidate.interview_history.append(
                    report
                )

                # Save to PostgreSQL
                save_interview(
                    report,
                    candidate
                )

        st.session_state.interview_finished = True

        st.rerun()
# ==================================================
# Evaluation Screen
# ==================================================

if st.session_state.interview_finished:

    st.success("✅ Interview Completed Successfully!")

    render_evaluation(
        st.session_state.report
    )

    st.markdown("<br>", unsafe_allow_html=True)

    show_history = st.toggle(
        "📜 Show Interview History"
    )

    if show_history:

        render_history(
            candidate.interview_history
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔄 Start New Interview",
            use_container_width=True
        ):

            # Reset interview state
            candidate.interview_started = False
            candidate.interviewer = None
            candidate.current_report = None

            # Clear current session values
            st.session_state.question = ""
            st.session_state.report = None
            st.session_state.interview_finished = False

            st.rerun()

    with col2:

        st.button(
            "📄 Download Report (Coming Soon)",
            use_container_width=True,
            disabled=True
        )