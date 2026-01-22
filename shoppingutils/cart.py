def calculate_total_price(cart):
    for item in cart:
        total = sum(item["price"])
        return total
