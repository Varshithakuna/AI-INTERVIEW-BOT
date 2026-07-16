import streamlit as st


def render_interview(question):

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # Header
    # ==================================================

    st.markdown("""
    <div class="card">

    <h2 style="margin-bottom:5px;">
        🤖 AI Interview
    </h2>

    <p style="color:#94A3B8;">
        Answer naturally. The AI will evaluate your communication,
        technical knowledge and problem-solving skills.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ==================================================
    # Progress
    # ==================================================

    st.markdown("### 📈 Interview Progress")

    st.progress(0.25)

    st.caption("Question 1 of 4")

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # AI Question
    # ==================================================

    st.markdown("### 🤖 AI Interviewer")

    st.info(question)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # Answer Section
    # ==================================================

    st.markdown("### 💬 Your Answer")

    answer = st.text_area(
        "",
        height=220,
        placeholder="Explain your answer in detail..."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # Buttons
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:

        submit = st.button(
            "📤 Submit Answer",
            use_container_width=True
        )

    with col2:

        end = st.button(
            "🛑 End Interview",
            use_container_width=True
        )

    return answer, submit, end