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

## What I learned
- How to use the Anthropic API and free Hugging Face models
- How to safely store secrets using `.env` files and `.gitignore`
- Git basics: init, add, commit, push
- How GitHub's secret scanning protects against leaked API keys
- How to give a chatbot conversation memory