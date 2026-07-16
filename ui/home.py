import streamlit as st


def render_home(candidate):

    left, right = st.columns([1, 1], gap="large")

    # ==================================================
    # Candidate Details Card
    # ==================================================
    with left:

        st.markdown("""
        <div class="card">
            <h2>👤 Candidate Details</h2>
            <p style="color:#94A3B8;margin-top:-8px;margin-bottom:25px;">
                Enter your information to personalize your AI interview experience.
            </p>
        </div>
        """, unsafe_allow_html=True)

        candidate.name = st.text_input(
            "👤 Full Name",
            value=candidate.name,
            placeholder="Enter your full name"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("#### 📄 Resume")

        candidate.resume = st.file_uploader(
            "Upload your resume",
            type=["pdf"],
            label_visibility="collapsed"
        )

        if candidate.resume is None:

            st.info(
                "📂 Drag & Drop your resume here or click **Browse Files**.\n\n"
                "Supported format: **PDF**"
            )

        else:

            st.success("✅ Resume uploaded successfully!")

            st.caption(f"📄 {candidate.resume.name}")

    # ==================================================
    # Interview Configuration Card
    # ==================================================
    with right:

        st.markdown("""
        <div class="card">
            <h2>⚙ Interview Configuration</h2>
            <p style="color:#94A3B8;margin-top:-8px;margin-bottom:25px;">
                Configure your interview before getting started.
            </p>
        </div>
        """, unsafe_allow_html=True)

        candidate.role = st.selectbox(
            "🎯 Target Role",
            (
                "Software Engineer",
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer",
                "AI Engineer",
                "Data Scientist"
            )
        )

        candidate.experience = st.selectbox(
            "💼 Experience Level",
            (
                "Fresher",
                "0-2 Years",
                "2-5 Years",
                "5+ Years"
            )
        )

        interview_type = st.selectbox(
            "📝 Interview Type",
            (
                "Technical",
                "HR",
                "Mixed"
            )
        )

        difficulty = st.selectbox(
            "🔥 Difficulty Level",
            (
                "Easy",
                "Medium",
                "Hard"
            )
        )

        total_questions = st.slider(
            "❓ Number of Questions",
            min_value=5,
            max_value=20,
            value=10,
            step=1
        )

        interview_mode = st.radio(
            "🎤 Interview Mode",
            (
                "💬 Chat",
                "🎤 Voice (Coming Soon)"
            ),
            horizontal=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h3 style="margin-top:0;">📊 Interview Summary</h3>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Role", candidate.role)
            st.metric("Questions", total_questions)

        with col2:
            st.metric("Difficulty", difficulty)
            st.metric("Mode", interview_mode.replace("🎤 ", "").replace("💬 ", ""))

        st.markdown("</div>", unsafe_allow_html=True)

    return (
        candidate,
        interview_type,
        difficulty,
        total_questions,
        interview_mode
    )