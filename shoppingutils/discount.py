def apply_discount(cart, discount):
    discount_rate = 1 -(discount /100)
    return [{"product": item["product"], "price": round(item["price"] * discount_rate, 2)}]
