import requests
from telegram import Bot
# Directly adding the token (NOT RECOMMENDED)
TOKEN = "7835773974:AAFYYVRmD7hWB4rudT99w3U63066ByWRg2E
# Editable settings
EXCHANGE_RATE = 1.0  # Change as needed
MY_PERCENTAGE = 10  # Change as needed (in %)
DELIVERY_COSTS = {
    "clothing": 20,  # Change as needed
    "shoes": 30,  # Change as needed
    "bags": 40,  # Change as needed
}

def fetch_product_details(url):
    # Function to scrape product details from the given URL
    # This is just a placeholder, actual scraping code will be added later
    return {
        "name": "Example Product",
        "price": 1000,  # Example price
        "sizes": ["S", "M", "L"],
        "composition": "100% Cotton"
    }

def calculate_price(product):
    base_price = product["price"] * EXCHANGE_RATE
    final_price = base_price + (base_price * MY_PERCENTAGE / 100) + DELIVERY_COSTS.get("clothing", 0)
    return final_price

def send_to_telegram(product, chat_id, bot_token):
    bot = Bot(token=bot_token)
    message = f"""
    🏷 *{product['name']}*
    💰 Price: ${calculate_price(product)}
    📏 Sizes: {', '.join(product['sizes'])}
    🏗 Composition: {product['composition']}
    """
    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")

# Example Usage
if __name__ == "__main__":
    test_product = fetch_product_details("https://example.com/product")
    print("Final Price:", calculate_price(test_product))
