from openai import OpenAI #type: ignore
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def paraphrase_sentences(sentences):
    results = []
    for sentence in sentences:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": "You are an assistant that paraphrases text in academic style."},
                    {"role": "user", "content": f"Paraphrase the following sentence:\n\n{sentence}"}
                ],
                temperature=0.7
            )
            paraphrased = response.choices[0].message.content.strip()
            results.append(paraphrased)
        except Exception as e:
            results.append(f"[Error: {str(e)}]")
    return results
