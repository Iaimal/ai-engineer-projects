# Semantic Search over Notes

A command-line tool that searches a folder of `.txt` notes by **meaning**, not
exact keywords, using sentence embeddings.

## Why this is different from normal (keyword) search

A keyword search for `"optimize a model"` would find nothing in a note that
says *"gradient descent minimizes a loss function"* — no shared words.
This tool finds it anyway, because it compares the *meaning* of your query
against the *meaning* of each note using sentence embeddings and cosine
similarity, rather than matching text.

## How it works

1. Each note (and your search query) is converted into a 384-number vector
   using the `all-MiniLM-L6-v2` sentence-transformer model.
2. The query's vector is compared against every note's vector using
   **cosine similarity** — a score from 0 (unrelated) to 1 (same meaning).
3. The note with the highest score is returned.
4. If the best score is still below a minimum threshold (0.2), the tool
   says "no good match found" instead of confidently returning an
   irrelevant note.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Drop any `.txt` files into the `notes/` folder (a few examples are included),
then run:

```bash
python search.py --notes_dir notes
```

Example session:

```
Search your notes: How do I stop my model from overfitting?
Best match (0.36) — overfitting.txt:
  Overfitting occurs when a machine learning model learns the training
  data too well, including its noise, and fails to generalize to new,
  unseen data.

Search your notes: best pizza toppings
No good match found in your notes.
```

## Project structure

```
semantic-search-notes/
├── search.py           # main script
├── requirements.txt
├── notes/               # drop your own .txt notes here
└── README.md
```

## Limitations / next steps

- Loads the entire notes folder into memory at once — fine for small note
  collections, would need a real vector database (e.g. Chroma, Pinecone)
  to scale to thousands of documents.
- Only supports plain `.txt` files for now — PDFs/Markdown would need a
  text-extraction step first.
- This is the retrieval half of a RAG (Retrieval-Augmented Generation)
  pipeline — the natural next step is feeding the retrieved note into an
  LLM to generate a full answer instead of just returning the raw note.

## Built as part of my AI Engineer learning roadmap.
