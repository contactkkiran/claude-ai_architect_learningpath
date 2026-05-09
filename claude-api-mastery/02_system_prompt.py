import os
from pathlib import Path

from dotenv import load_dotenv
import anthropic

load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY is missing. Add it to claude-api-mastery/.env")

client = anthropic.Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,                  # max length of response
    system="""You are FinBot, an AI financial assistant for Indian retail investors.
You explain concepts simply, in plain English.
Always mention risk factors when discussing investments.
Never give specific buy/sell recommendations — only education.""",
    messages=[
        {"role": "user", "content": "What is a mutual fund?"}
    ],
)

# Next, print the response to see the system prompt in action.
print(response.content[0].text)
