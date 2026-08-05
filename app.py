import streamlit as st
from google import genai

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Gemini AI Chatbot")
st.caption("Powered by Google Gemini")

with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )

    model = st.selectbox(
        "Select Model",
        [
            "gemini-3.6-flash",
        ]
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask anything...")

if prompt:

    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
        st.stop()


    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)


    try:

        client = genai.Client(api_key=api_key)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                answer = response.text

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        st.error(f"Error: {e}")