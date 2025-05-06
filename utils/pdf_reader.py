import pdfplumber
import nltk
import re

nltk.download('punkt')
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
