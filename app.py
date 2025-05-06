import streamlit as st
from utils.pdf_reader import extract_sentences_from_pdf
from utils.semantic_search import find_similar_sentences
from utils.gpt_paraphrase import paraphrase_sentences

import os
from dotenv import load_dotenv
import html
import streamlit.components.v1 as components

# Load API Key from .env
load_dotenv()

st.set_page_config(page_title="PDF Journal Assistant", layout="wide")
st.title("PDF Journal Assistant with Semantic Search + GPT Paraphrasing")

# --- File Upload ---
uploaded_files = st.file_uploader("Upload one or more journal PDFs", type=["pdf"], accept_multiple_files=True)

# --- Query Input ---
search_query = st.text_input("🔍 Enter your search query (e.g., 'fungicide against pathogen')")

# --- Start Processing ---
if uploaded_files and search_query:
    all_sentences = []
    st.subheader("📖 Extracting Sentences...")

    for file in uploaded_files:
        sentences = extract_sentences_from_pdf(file)
        all_sentences.extend(sentences)

    st.success(f"Extracted {len(all_sentences)} total sentences from {len(uploaded_files)} files.")

    # --- Semantic Search ---
    st.subheader("🧠 Finding Relevant Sentences...")
    top_matches = find_similar_sentences(search_query, all_sentences, top_n=20)

    selected_sentences = []
    for i, (score, sent) in enumerate(top_matches):
        if st.checkbox(f"{sent} (Score: {score:.2f})", key=i):
            selected_sentences.append(sent)

    # --- Paraphrase Section ---
    if selected_sentences:
        st.subheader("✍️ Paraphrase Selected Sentences")
        if st.button("Paraphrase Now"):
            with st.spinner("Paraphrasing with GPT..."):
                paraphrased = paraphrase_sentences(selected_sentences)
            st.success("Done!")

            for i, (orig, para) in enumerate(zip(selected_sentences, paraphrased)):
                safe_para = html.escape(para)
                st.markdown(f"### ✍️ Result {i+1}")
                st.markdown(f"**Original:** {orig}")
                st.markdown(f"**Paraphrased:** {para}")

            copy_html = f"""
                <input type=\"text\" value=\"{safe_para}\" id=\"copyText{i}\" style=\"position:absolute; left:-9999px;\">
                <button onclick=\"var copyText = document.getElementById('copyText{i}'); copyText.select(); document.execCommand('copy');\">📋 Copy</button>
                """
            components.html(copy_html, height=40)
            st.markdown(f"Click the button to copy the paraphrased text to clipboard.")
else:
    st.info("Upload PDF files and enter a search query to begin.")
