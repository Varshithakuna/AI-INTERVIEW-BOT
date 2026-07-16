import streamlit as st


def section_title(title, icon="✨"):

    st.markdown(
        f"""
        <div class="card">
            <h3>{icon} {title}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )


def success_message(message):

    st.success(message)


def info_message(message):

    st.info(message)


def warning_message(message):

    st.warning(message)