"""
Semantic Search over Notes
--------------------------
Searches a folder of .txt notes by MEANING (not keywords) using sentence embeddings.

Usage:
    python search.py --notes_dir notes

Then type any question at the prompt. Type 'exit' to quit.
"""

import os
import argparse
import numpy as np
from sentence_transformers import SentenceTransformer, util

MIN_SCORE = 0.2  # below this, we say "no good match" instead of guessing


def load_notes(notes_dir: str):
    """Read every .txt file in notes_dir into a list of (filename, content) pairs."""
    notes = []
    filenames = []
    for fname in sorted(os.listdir(notes_dir)):
        if fname.endswith(".txt"):
            path = os.path.join(notes_dir, fname)
            with open(path, "r", encoding="utf-8") as f:
                notes.append(f.read().strip())
                filenames.append(fname)
    return notes, filenames


def search(query, notes, note_embeddings, model, filenames):
    """Return the best-matching note (and its filename + score) for a query."""
    query_embedding = model.encode(query)
    scores = util.cos_sim(query_embedding, note_embeddings)
    best_idx = int(np.argmax(scores))
    return filenames[best_idx], notes[best_idx], scores[0][best_idx].item()


def main():
    parser = argparse.ArgumentParser(description="Semantic search over a folder of notes.")
    parser.add_argument("--notes_dir", default="notes", help="Folder containing .txt notes")
    args = parser.parse_args()

    print(f"Loading notes from '{args.notes_dir}'...")
    notes, filenames = load_notes(args.notes_dir)

    if not notes:
        print(f"No .txt files found in '{args.notes_dir}'. Add some notes and try again.")
        return

    print(f"Loaded {len(notes)} notes: {filenames}")
    print("Loading embedding model (all-MiniLM-L6-v2)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Encoding notes...")
    note_embeddings = model.encode(notes)

    print("\nReady! Type a question about your notes (or 'exit' to quit).\n")
    while True:
        query = input("Search your notes: ").strip()
        if query.lower() == "exit":
            break
        if not query:
            continue

        filename, content, score = search(query, notes, note_embeddings, model, filenames)

        if score < MIN_SCORE:
            print("No good match found in your notes.\n")
        else:
            print(f"Best match ({score:.2f}) — {filename}:")
            print(f"  {content}\n")


if __name__ == "__main__":
    main()
