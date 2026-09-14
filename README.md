# AI Engineer Projects

Learning projects built while working through my AI Engineer roadmap.

## Projects

### 1. Text Summarizer (`test.py`)
A simple script that sends text to an AI model and returns a 3-bullet-point summary.

**How to run:**
1. Install dependencies: `pip install anthropic python-dotenv`
2. Create a `.env` file with your own `ANTHROPIC_API_KEY`
3. Run: `python test.py`

### 2. Sentiment Classifier (`sentiment_classifier.ipynb`)
Classifies text as Positive, Negative, or Neutral using a free, open-source model (Phi-3-mini) via Google Colab.

### 3. CLI Chatbot (`chatbot.ipynb`)
A command-line chatbot that remembers conversation history across turns.

**How it works:**
- Keeps a growing list of messages (as role/content pairs)
- Sends the entire conversation history to the model each turn, so it has context

**How to run:**
1. Open in Google Colab
2. Enable GPU: Runtime → Change runtime type → T4 GPU
3. Run all cells in order
4. Type messages; type "exit" to quit

**Known Limitation:**
Uses a small, free, open-source model (Phi-3-mini) for cost reasons.
Correctly remembers conversation history, but sometimes drifts
off-topic in its responses — a known limitation of smaller models
compared to production LLMs like Claude/GPT.

### 4. Combined CLI Tool (`combined_tool.ipynb`)
A single menu-driven tool that merges the summarizer, sentiment classifier, and chatbot into one script.

**How it works:**
- Loads one shared Phi-3-mini model (`generator`) used by all three features
- Menu loop lets the user pick: summarize text, classify sentiment, chat, or exit
- Chat mode keeps its own conversation history, same as the standalone chatbot

**How to run:**
1. Open in Google Colab
2. Enable GPU: Runtime → Change runtime type → T4 GPU
3. Run the model-loading cell first, then the menu cell
4. Choose an option (1-4) when prompted

### 5. Character-Level Tokenizer — LLM Data Pipeline Foundations (`nanogpt_foundations.ipynb`)
Implements the data preparation layer behind language models, built while
studying transformer/LLM internals.

**Includes:**
- Character-level `encode`/`decode` functions
- Conversion to a PyTorch tensor
- Train/validation split
- Input/target windowing for next-token prediction

**Does not include:** the model architecture or training loop — scoped
intentionally as a foundational understanding exercise, not a complete
generative model.

**How to run:**
1. Open in Google Colab
2. Run all cells in order (Runtime → Run all)
3. Modify the `text` variable to try it with different input text

### 6. Semantic Search Over Notes (`semantic-search-notes/`)
A tool that searches a folder of personal `.txt` notes by **meaning**, not
exact keywords, using sentence embeddings and cosine similarity. Built with
two interfaces: a command-line version and a Streamlit web app.

**Why this is different from keyword search:**
A keyword search for "optimize a model" finds nothing in a note that says
"gradient descent minimizes a loss function" — no shared words. This tool
finds it anyway, because it compares the *meaning* of the query against the
*meaning* of each note.

**How it works:**
- Loads a free embedding model (`all-MiniLM-L6-v2`) via `sentence-transformers`
- Reads every `.txt` file from a `notes/` folder
- Converts each note (and the search query) into a 384-number embedding vector
- Compares the query against every note using cosine similarity (0 = unrelated, 1 = identical meaning)
- Returns the highest-scoring note, along with its filename and similarity score
- Includes a relevance threshold (`MIN_SCORE = 0.2`) — returns "no good match found" instead of confidently returning an irrelevant note when nothing actually matches well

**Two interfaces:**
- **CLI** (`search.py`) — terminal-based, loops until you type "exit"
  ```bash
  pip install -r requirements.txt
  python search.py --notes_dir notes
  ```
- **Web app** (`app.py`) — Streamlit interface with a sidebar listing loaded notes, a search box, and cached model/data loading so it doesn't reload on every query
  ```bash
  pip install -r requirements.txt
  streamlit run app.py
  ```

**Example session (CLI):**
```
Search your notes: How do I stop my model from overfitting?
Best match (0.36) — overfitting.txt:
  Overfitting occurs when a machine learning model learns the training
  data too well, including its noise, and fails to generalize to new,
  unseen data.

Search your notes: best pizza toppings
No good match found in your notes.
```

**Known Limitations:**
- Loads the entire notes folder into memory at once — fine for a small
  collection, would need a real vector database (e.g. Chroma, Pinecone) to
  scale to thousands of documents
- Only supports plain `.txt` files — PDFs/Markdown would need a
  text-extraction step first
- This is the **retrieval** half of a RAG (Retrieval-Augmented Generation)
  pipeline — the natural next step (Month 4) is feeding the retrieved note
  into an LLM to generate a full answer instead of just returning the raw note

## What I learned
- How to use the Anthropic API and free Hugging Face models
- How to safely store secrets using `.env` files and `.gitignore`
- Git basics: init, add, commit, push
- How GitHub's secret scanning protects against leaked API keys
- How to give a chatbot conversation memory
- Combining multiple features into one tool using if/elif branching
- Structuring a menu-driven CLI program with a main loop
- Character-level tokenization and the next-token prediction training signal behind language models
- How embeddings capture semantic meaning, and how cosine similarity measures it
- Why a relevance threshold matters in search tools (avoiding forced, low-confidence matches)
- Building the same tool with two different interfaces (CLI with `argparse`, web app with Streamlit) from shared core logic
- Using Streamlit's caching (`@st.cache_resource`, `@st.cache_data`) to avoid reloading a model or re-reading files on every interaction