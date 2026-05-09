import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv
from products import get_price, check_inventory, search_products, get_offers

load_dotenv()
client = Anthropic()

# ─────────────────────────────────────────
# PART 1 — Tell Claude what tools exist
# ─────────────────────────────────────────
tools = [
    {
        "name": "get_price",
        "description": "Get the price of a product. Use this when user asks about price, cost, or how much a product costs.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "The name of the product. Example: Nike Air Max"
                }
            },
            "required": ["product_name"]
        }
    },
    {
        "name": "check_inventory",
        "description": "Check if a product is in stock. Use this when user asks about availability or stock.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "The name of the product. Example: Adidas Ultraboost"
                }
            },
            "required": ["product_name"]
        }
    },
    {
        "name": "search_products",
        "description": "Search products by category and maximum price. Use this when user wants to browse or filter products.",
        "input_schema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Product category. Examples: men_shoes, women_shoes, unisex_shoes"
                },
                "max_price": {
                    "type": "integer",
                    "description": "Maximum price in rupees. Example: 5000"
                }
            },
            "required": ["category", "max_price"]
        }
    },
    {
        "name": "get_offers",
        "description": "Get all products with active discounts. Use this when user asks about deals, offers, or discounts.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]


# ─────────────────────────────────────────
# PART 2 — Run whichever tool Claude picks
# ─────────────────────────────────────────
def run_tool(tool_name: str, tool_input: dict) -> str:

    print(f"\n⚙️  Claude is calling: {tool_name}")
    print(f"📥 Inputs: {tool_input}")

    if tool_name == "get_price":
        result = get_price(tool_input["product_name"])

    elif tool_name == "check_inventory":
        result = check_inventory(tool_input["product_name"])

    elif tool_name == "search_products":
        result = search_products(
            tool_input["category"],
            tool_input["max_price"]
        )

    elif tool_name == "get_offers":
        result = get_offers()

    else:
        result = {"error": f"Unknown tool: {tool_name}"}

    print(f"📤 Result: {result}")
    return json.dumps(result)


# ─────────────────────────────────────────
# PART 3 — The Agent Loop
# ─────────────────────────────────────────
def run_agent(user_message: str) -> None:

    print(f"\n{'='*50}")
    print(f"👤 You: {user_message}")
    print(f"{'='*50}")

    messages = [
        {"role": "user", "content": user_message}
    ]

    while True:

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system="You are a helpful e-commerce assistant for a shoe store. Help customers find products, check prices, stock and offers. Always mention prices in Indian Rupees (₹).",
            tools=tools,
            messages=messages
        )

        print(f"\n🧠 Claude is thinking... stop reason: {response.stop_reason}")

        # Claude wants to call a tool
        if response.stop_reason == "tool_use":

            messages.append({
                "role": "assistant",
                "content": response.content
            })

            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = run_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            messages.append({
                "role": "user",
                "content": tool_results
            })

        # Claude has final answer
        elif response.stop_reason == "end_turn":

            for block in response.content:
                if hasattr(block, "text"):
                    print(f"\n🤖 Agent: {block.text}")
            break


# ─────────────────────────────────────────
# PART 4 — Start the program
# ─────────────────────────────────────────
if __name__ == "__main__":
    run_agent("What are the available offers?") 