import pdfplumber
import spacy
import re

# Load spaCy model (automatically downloads in cloud if in requirements.txt)
nlp = spacy.load("en_core_web_sm")

def extract_sentences_from_pdf(file):
    all_text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"

    # Basic cleaning
    all_text = re.sub(r'\s+', ' ', all_text)

    # Sentence splitting using spaCy
    doc = nlp(all_text)
    sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 40]

    return sentences
