#  Mental Model First
# Tools let Claude call your functions.
# Without tools → Claude only talks
# With tools    → Claude talks + takes actions

# Real World Example
# User: "What is the weather in Hyderabad?"

# Without tools → Claude says "I don't know current weather"
# With tools    → Claude calls your get_weather() function → returns real data

import anthropic
import json
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

# Step 1 — Define the tool
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["city"]
        }
    }
]

# Step 2 — Your actual function
def get_weather(city):
    # Fake data for now — real app would call a weather API
    return f"Weather in {city}: 32°C, Sunny"

# Step 3 — Send to Claude
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    temperature=0.0,
    tools=tools,
    messages=[
        {"role": "user", "content": "What is the weather in Hyderabad?"}
    ]
)

# Step 4 — Check if Claude wants to call a tool
if response.stop_reason == "tool_use":
    tool_call = response.content[1]
    tool_name = tool_call.name
    tool_input = tool_call.input

    print(f"Claude wants to call: {tool_name}")
    print(f"With input: {tool_input}")

    # Step 5 — Run your function
    result = get_weather(tool_input["city"])
    print(f"Function result: {result}")