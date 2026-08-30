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

## What I learned
- How to use the Anthropic API and free Hugging Face models
- How to safely store secrets using `.env` files and `.gitignore`
- Git basics: init, add, commit, push
- How GitHub's secret scanning protects against leaked API keys
- How to give a chatbot conversation memory
- Combining multiple features into one tool using if/elif branching
- Structuring a menu-driven CLI program with a main loop
- Character-level tokenization and the next-token prediction training signal behind language models