import streamlit as st


def render_hero():

    st.markdown(
        """
<div style="text-align:center; margin-top:20px; margin-bottom:30px;">

<h1 style="color:white; font-size:48px; margin-bottom:10px;">
🎤 AI Interview Partner
</h1>

<p style="color:#94A3B8; font-size:18px;">
Practice AI-powered interviews tailored to your resume.<br>
Get resume-based questions, instant AI feedback, and detailed evaluation reports.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🤖 AI Model", "Llama 3.3")

    with col2:
        st.metric("📄 Resume", "Supported")

    with col3:
        st.metric("🎯 Interview Types", "3")

    with col4:
        st.metric("📊 Evaluation", "Instant")

    st.markdown("<br>", unsafe_allow_html=True)