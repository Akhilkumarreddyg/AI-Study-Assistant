import streamlit as st
from graph import study_graph

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")

st.write(
    "Enter any topic or question and the AI will explain it in a simple way."
)

question = st.text_input("Enter your question or topic:")

if st.button("Explain"):
    if question:
        with st.spinner("AI is thinking..."):
            result = study_graph.invoke(
                {
                    "question": question,
                    "answer": ""
                }
            )

        st.subheader("AI Explanation")
        st.write(result["answer"])

    else:
        st.warning("Please enter a question.")