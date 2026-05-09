# This is our fake e-commerce database
# In real world this would be MySQL / MongoDB

PRODUCTS = [
    {
        "id": 1,
        "name": "Nike Air Max",
        "category": "men_shoes",
        "price": 4999,
        "stock": 3,
        "discount": 10
    },
    {
        "id": 2,
        "name": "Adidas Ultraboost",
        "category": "men_shoes",
        "price": 6999,
        "stock": 0,
        "discount": 0
    },
    {
        "id": 3,
        "name": "Puma Running Shoes",
        "category": "men_shoes",
        "price": 3499,
        "stock": 12,
        "discount": 15
    },
    {
        "id": 4,
        "name": "Nike Women's Court",
        "category": "women_shoes",
        "price": 4499,
        "stock": 7,
        "discount": 5
    },
    {
        "id": 5,
        "name": "Adidas Samba",
        "category": "unisex_shoes",
        "price": 5999,
        "stock": 2,
        "discount": 0
    }
]


def get_price(product_name: str) -> dict:
    """Get price of a product by name"""
    for product in PRODUCTS:
        if product_name.lower() in product["name"].lower():
            return {
                "found": True,
                "product": product["name"],
                "price": product["price"],
                "discount": product["discount"],
                "final_price": product["price"] - (product["price"] * product["discount"] // 100)
            }
    return {"found": False, "message": f"{product_name} not found"}


def check_inventory(product_name: str) -> dict:
    """Check if product is in stock"""
    for product in PRODUCTS:
        if product_name.lower() in product["name"].lower():
            return {
                "found": True,
                "product": product["name"],
                "in_stock": product["stock"] > 0,
                "quantity": product["stock"]
            }
    return {"found": False, "message": f"{product_name} not found"}


def search_products(category: str, max_price: int) -> dict:
    """Search products by category and max price"""
    results = [
        p for p in PRODUCTS
        if category.lower() in p["category"].lower()
        and p["price"] <= max_price
    ]
    return {
        "count": len(results),
        "products": [
            {"name": p["name"], "price": p["price"], "in_stock": p["stock"] > 0}
            for p in results
        ]
    }


def get_offers() -> dict:
    """Get all products with active discounts"""
    offers = [p for p in PRODUCTS if p["discount"] > 0]
    return {
        "count": len(offers),
        "offers": [
            {
                "name": p["name"],
                "original_price": p["price"],
                "discount_percent": p["discount"],
                "final_price": p["price"] - (p["price"] * p["discount"] // 100)
            }
            for p in offers
        ]
    }