def check_availability(cart, inventory):
    needed = {}
    for item in cart:
        p = item["product"]
        needed[p] = needed.get(p, 0) + 1
    for product, quantity in needed.items():
        if product not in inventory or inventory[product] < quantity:
            return Fales
    return True
