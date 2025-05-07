import streamlit as st
from utils.pdf_reader import extract_sentences_from_pdf
from utils.semantic_search import find_similar_sentences
from utils.gpt_paraphrase import paraphrase_sentences

import os
from dotenv import load_dotenv
import html
 

# Load API Key from .env
load_dotenv()

st.set_page_config(page_title="PDF Journal Assistant", layout="wide")
st.title("PDF Journal Assistant")

st.markdown("---")

# --- File Upload ---
uploaded_files = st.file_uploader("Upload one or more journal PDFs", type=["pdf"], accept_multiple_files=True)

# --- Query Input ---
search_query = st.text_input("🔍 Enter your search query (e.g., 'fungicide against pathogen')")

st.markdown("---")

# --- Start Processing ---
if uploaded_files and search_query:
    all_sentences = []
    st.subheader("📖 Extracting Sentences...")

    for file in uploaded_files:
        sentences = extract_sentences_from_pdf(file)
        all_sentences.extend(sentences)

    st.success(f"Extracted {len(all_sentences)} total sentences from {len(uploaded_files)} files.")

    st.markdown("---")

    # --- Semantic Search ---
    st.subheader("🧠 Finding Relevant Sentences...")
    st.markdown("**Select the sentences you want to paraphrase from the results below.**")

    top_matches = find_similar_sentences(search_query, all_sentences, top_n=10)
    selected_sentences = []


    for i, (score, sent) in enumerate(top_matches):
        sent = sent.replace("\n", " ").replace("  ", " ").strip()  # Clean newlines and spacing
        if score >= 0.65:
            display_text = f'"{sent}" (Score: {score:.2f})'
            if st.checkbox(display_text, key=f"sent_{i}"):
                selected_sentences.append(sent)
    
    st.markdown("---")

    # --- Paraphrase Section ---
    if selected_sentences:
        st.subheader("✍️ Paraphrase Selected Sentences")
        st.info("Select sentences to paraphrase and click 'Paraphrase Now'.")
        if st.button("Paraphrase Now"):
            with st.spinner("Paraphrasing with GPT..."):
                paraphrased = paraphrase_sentences(selected_sentences)
            st.success("Done!")

            for i, (orig, para) in enumerate(zip(selected_sentences, paraphrased)):
                safe_para = html.escape(para)
                st.markdown(f"### ✍️ Result {i+1}")
                st.markdown(f"**Original:** {orig}")
                st.markdown(f"**Paraphrased:** {para}")
                st.code(para, language="text")
                st.markdown("---")

        
else:       
    st.info("Upload PDF files and enter a search query to begin.")
