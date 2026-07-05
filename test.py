import os
from dotenv import load_dotenv
import anthropic

load_dotenv()  # reads your .env file

client = anthropic.Anthropic()  # automatically finds your key

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Explain photosynthesis in one sentence."}
    ]
)

print(message.content[0].text)