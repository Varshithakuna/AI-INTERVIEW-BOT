import streamlit as st


def render_history(interview_history):

    st.markdown("---")

    st.markdown("""
    <div class="card">
        <h2>📜 Interview History</h2>
    </div>
    """, unsafe_allow_html=True)

    if len(interview_history) == 0:

        st.info("No interviews completed yet.")

        return

    # Show latest interview first
    for report in reversed(interview_history):

        with st.container():

            st.markdown("""
            <div class="card">
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"👤 **Candidate:** {report['candidate_name']}")
                st.write(f"💼 **Role:** {report['role']}")
                st.write(f"❓ **Questions:** {report['questions_answered']}")

            with col2:

                st.metric(
                    "Overall Score",
                    f"{report['overall_score']}%"
                )

                st.success(report["recommendation"])

            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)