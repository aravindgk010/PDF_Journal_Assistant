from sentence_transformers import SentenceTransformer #type: ignore
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import zipfile

# Unzip the model if it doesn't already exist
#if not os.path.exists('local_model'):
#    with zipfile.ZipFile('local_model.zip', 'r') as zip_ref:
#        zip_ref.extractall('local_model')

#model = SentenceTransformer('local_model')

# Load a compact model for speed
model = SentenceTransformer('all-MiniLM-L6-v2')

def find_similar_sentences(query, sentences, top_n=10):
    if not sentences:
        return []

    # Embed the query and the sentences
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)
    query_embedding = model.encode([query], convert_to_tensor=True)

    # Compute cosine similarities
    similarities = cosine_similarity(query_embedding, sentence_embeddings)[0]

    # Zip with original sentences and sort by similarity
    scored_sentences = list(zip(similarities, sentences))
    scored_sentences.sort(reverse=True, key=lambda x: x[0])

    return scored_sentences[:top_n]
