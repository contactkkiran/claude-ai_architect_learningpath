# E-Commerce Shoe Store Agent

This project is a simple Claude-powered e-commerce assistant for a shoe store.
The agent can answer customer questions about product prices, stock availability,
filtered product searches, and current offers.

## Files

- `agent.py` - Runs the Claude agent loop and defines the tools Claude can use.
- `products.py` - Contains the fake product dataset and product helper functions.

## How It Works

1. The user asks a shopping question.
2. Claude reads the request and decides whether it needs a tool.
3. If a tool is needed, Claude calls one of the product tools from `agent.py`.
4. `agent.py` sends the tool input to a function in `products.py`.
5. The function searches the product dataset and returns structured data.
6. Claude uses the tool result to produce a final customer-friendly answer.

## Setup Steps

1. Open the project folder:

   ```bash
   cd ecommerce-agent
   ```

2. Install the required Python packages:

   ```bash
   pip install anthropic python-dotenv
   ```

3. Create a `.env` file in the `ecommerce-agent` folder:

   ```bash
   ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Run the agent:

   ```bash
   python agent.py
   ```

By default, `agent.py` runs this sample question:

```python
run_agent("What are the available offers?")
```

You can change this line to test other customer questions.

## Example Questions

- What is the price of Nike Air Max?
- Is Adidas Ultraboost in stock?
- Show me men shoes under 5000.
- What are the available offers?
- Do you have any discounted shoes?

## Agent Tools

| Tool | Purpose | Example Input |
| --- | --- | --- |
| `get_price` | Gets a product price, discount, and final price. | `{"product_name": "Nike Air Max"}` |
| `check_inventory` | Checks whether a product is in stock. | `{"product_name": "Adidas Ultraboost"}` |
| `search_products` | Searches products by category and maximum price. | `{"category": "men_shoes", "max_price": 5000}` |
| `get_offers` | Returns all products that have active discounts. | `{}` |

## Product Dataset

The dataset is stored in `products.py` as a Python list named `PRODUCTS`.

| ID | Product | Category | Price | Stock | Discount |
| --- | --- | --- | ---: | ---: | ---: |
| 1 | Nike Air Max | `men_shoes` | ₹4,999 | 3 | 10% |
| 2 | Adidas Ultraboost | `men_shoes` | ₹6,999 | 0 | 0% |
| 3 | Puma Running Shoes | `men_shoes` | ₹3,499 | 12 | 15% |
| 4 | Nike Women's Court | `women_shoes` | ₹4,499 | 7 | 5% |
| 5 | Adidas Samba | `unisex_shoes` | ₹5,999 | 2 | 0% |

## Product Fields

- `id` - Unique product ID.
- `name` - Product name shown to customers.
- `category` - Product category used for filtering.
- `price` - Product price in Indian Rupees.
- `stock` - Available quantity.
- `discount` - Discount percentage. A value greater than `0` means the product has an active offer.

## Current Offers

| Product | Original Price | Discount | Final Price |
| --- | ---: | ---: | ---: |
| Nike Air Max | ₹4,999 | 10% | ₹4,500 |
| Puma Running Shoes | ₹3,499 | 15% | ₹2,975 |
| Nike Women's Court | ₹4,499 | 5% | ₹4,275 |

## Notes

- This is a learning/demo project.
- The product database is fake and stored directly in code.
- In a real application, the data would usually come from a database such as MySQL, PostgreSQL, or MongoDB.
