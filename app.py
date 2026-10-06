import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Doubt Solving Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Doubt Solving Chatbot")
st.write("Ask your academic doubts and get simple explanations.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask your doubt here...")

if question:

    # Display user question
    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = ollama.chat(
                    model="llama3.2:latest",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an AI Doubt Solving Chatbot for college students. "
                                "Answer academic questions clearly and simply. "
                                "Explain concepts step by step when needed. "
                                "Use examples for better understanding. "
                                "If the question is related to programming, provide "
                                "correct and simple code when required."
                            )
                        },
                        *st.session_state.messages
                    ]
                )

                answer = response["message"]["content"]
                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(
                    "Ollama is not running or the model is not available.\n\n"
                    f"Error: {e}"
                )