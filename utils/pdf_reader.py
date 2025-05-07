import pdfplumber
import nltk
import os
import re

# Force NLTK to download 'punkt' to a local folder
nltk_data_path = os.path.join(os.path.dirname(__file__), '..', 'nltk_data')
nltk.download('punkt', download_dir=nltk_data_path)

# Tell NLTK to use the local data path
nltk.data.path.append(nltk_data_path)

from nltk.tokenize import sent_tokenize

def extract_sentences_from_pdf(file):
    all_text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"

    # Basic cleaning
    all_text = re.sub(r'\s+', ' ', all_text)

    # Sentence splitting
    sentences = sent_tokenize(all_text)
    
    # Optional: Filter out short or irrelevant sentences
    cleaned_sentences = [s.strip() for s in sentences if len(s.strip()) > 40]

    return cleaned_sentences
