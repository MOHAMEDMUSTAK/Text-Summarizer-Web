import streamlit as st
from collections import Counter
import re
# -----------------------------
# Text Summarization Function
# -----------------------------
def summarize_text(text, num_sentences=2):
    if not text.strip():
        return "Please enter valid text."
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\w+', text.lower())
    # Count word frequency
    word_frequencies = Counter(words)
    # Score each sentence
    sentence_scores = {}
    for sentence in sentences:
        score = 0
        for word in re.findall(r'\w+', sentence.lower()):
            score += word_frequencies.get(word, 0)
        sentence_scores[sentence] = score
    # Select top sentences
    top_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:num_sentences]
    return " ".join(top_sentences)
# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Text Summarizer", layout="centered")
st.title("AI Text Summarizer")
st.write("A simple extractive NLP-based text summarization tool built using Python and Streamlit.")
text_input = st.text_area("Enter your paragraph below:", height=200)
num_sentences = st.slider("Select number of sentences in summary:", 1, 5, 2)
if st.button("Summarize"):
    summary = summarize_text(text_input, num_sentences)
    st.subheader("Summary:")
    st.success(summary)
