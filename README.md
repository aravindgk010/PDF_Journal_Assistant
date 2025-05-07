# 📚 PDF Journal Assistant 🧠✍️  
An AI-powered assistant that extracts relevant sentences from research PDFs based on a custom query, performs semantic search, and paraphrases the results using OpenAI GPT models.

---

## 🚀 Features

- 📥 Upload one or more PDF journals
- 🔍 Search with any custom query (e.g., `"fungicide against pathogen"`)
- 🧠 Semantic sentence matching using embeddings
- ✍️ Paraphrasing in academic tone using GPT
- 📋 Copy paraphrased results with a single click
- 💡 Responsive UI with section toggles and progress feedback

---

## 📦 Installation

### 1. Clone the repository

git clone https://github.com/aravindgk010/PDF_Journal_Assistant.git
cd PDF_Journal_Assistant

### 2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add your OpenAI API key

create a .env file in the root directory

### 5. Run the App

streamlit run app.py

---

### Folder Structure

pdf-journal-assistant/
│
├── app.py                     # Main Streamlit app
├── .env                       # Your OpenAI API key
├── .gitignore
├── requirements.txt
├── README.md
├── utils/
│   ├── pdf_reader.py          # Extracts sentences from PDFs
│   ├── semantic_search.py     # Embedding-based similarity
│   └── gpt_paraphrase.py      # GPT paraphrasing logic

---

### Tech Stack

1. Python 3.10+
2. Streamlit
3. OpenAI GPT (via openai SDK)
4. PDFPlumber, NLTK
5. Sentence Transformers (semantic search)

---

### Credits

Made with ❤️ by Aravind
