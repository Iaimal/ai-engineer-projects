"""
Semantic Search over Notes — Web Interface (Streamlit)
--------------------------------------------------------
Run with:
    streamlit run app.py
"""

import streamlit as st
from sentence_transformers import SentenceTransformer, util
import numpy as np
import os

MIN_SCORE = 0.2
NOTES_DIR = "notes"


@st.cache_resource
def load_model():
    """Load the embedding model once and cache it across reruns."""
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_data
def load_notes(notes_dir):
    """Read every .txt file in notes_dir. Cached so it doesn't re-read on every keystroke."""
    notes, filenames = [], []
    for fname in sorted(os.listdir(notes_dir)):
        if fname.endswith(".txt"):
            with open(os.path.join(notes_dir, fname), "r", encoding="utf-8") as f:
                notes.append(f.read().strip())
                filenames.append(fname)
    return notes, filenames


def search(query, notes, note_embeddings, model, filenames):
    query_embedding = model.encode(query)
    scores = util.cos_sim(query_embedding, note_embeddings)
    best_idx = int(np.argmax(scores))
    return filenames[best_idx], notes[best_idx], scores[0][best_idx].item()


st.set_page_config(page_title="Semantic Search over Notes", page_icon="🔎")
st.title("🔎 Semantic Search over Notes")
st.caption("Searches your notes by meaning, not keywords — powered by sentence embeddings.")

model = load_model()
notes, filenames = load_notes(NOTES_DIR)

if not notes:
    st.error(f"No .txt files found in '{NOTES_DIR}/'. Add some notes and refresh.")
    st.stop()

note_embeddings = model.encode(notes)

st.sidebar.header("Loaded notes")
for fname in filenames:
    st.sidebar.write(f"📄 {fname}")

query = st.text_input("Ask a question about your notes:")

if query:
    filename, content, score = search(query, notes, note_embeddings, model, filenames)

    if score < MIN_SCORE:
        st.warning("No good match found in your notes.")
    else:
        st.success(f"Best match — **{filename}** (similarity: {score:.2f})")
        st.write(content)
