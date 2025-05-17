# app.py

import streamlit as st
from transformers import pipeline

import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
# Configure Streamlit page
st.set_page_config(page_title="Text-based Q&A", layout="centered")

st.title("📖 Text-based Question Answering")
st.write(
    "This application uses a fine-tuned Transformer model to answer questions based on the provided context paragraph."
)

# Load the QA model with caching to avoid reloading


@st.cache_resource
def load_qa_pipeline():
    model_name = "nhutan410/distilbert-finetuned-squadv2"
    return pipeline("question-answering", model=model_name)


qa_pipeline = load_qa_pipeline()

# Input fields
st.subheader("🔍 Provide Input")
context = st.text_area(
    label="Context Paragraph:",
    placeholder="Enter or paste your paragraph here...",
    height=200,
)

question = st.text_input(
    label="Question:",
    placeholder="Type your question based on the context..."
)

# Button to trigger answering
if st.button("Get Answer"):
    if context.strip() and question.strip():
        with st.spinner("Processing..."):
            try:
                result = qa_pipeline(question=question, context=context)
                st.success("✅ Answer:")
                st.markdown(f"**Answer:** {result['answer']}")
                st.markdown(f"**Confidence Score:** `{result['score']:.4f}`")
            except Exception as e:
                st.error(
                    f"⚠️ An error occurred while generating the answer: {e}")
    else:
        st.warning("⚠️ Please enter both the context and a question.")
