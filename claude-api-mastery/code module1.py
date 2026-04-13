from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Example 1: Basic API Call with System Prompt and Messages
# 1. Basic API Call
response = client.messages.create(
    model="claude-sonnet-4-6",       # which Claude model to use
    max_tokens=1024,                  # max length of response
    
    # 2. System Prompt — give Claude a role and rules
    system="""
You are a Claude API expert and Python developer.
Rules:
- Explain concepts in plain English
- No markdown formatting
- No headers, no bold, no bullet symbols
- Plain text only
- Keep it simple and short
""",
    # 3. Messages — the actual conversation
    messages=[
    {"role": "user", "content": "What is AI?"}
]
)

# 4. Print response
print(response.content[0].text)

#5. Tokens — how much was consumed
print(f"Tokens used: {response.usage.input_tokens} in / {response.usage.output_tokens} out")


# Example 2: More Complex Conversation  to generate ready api code with implementation details
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="""You are a senior Python developer and API expert. 
You have experience building production-ready APIs using FastAPI and Flask. 
Rules:
- Provide clear and concise explanations
- Use plain English, no technical jargon
- No markdown formatting, plain text only
- Focus on practical implementation details
""",
    messages=[
    {"role": "user", "content": "How do I build a simple API using FastAPI?"}
]
) 
print(response.content[0].text)      