def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}

def add_to_cart(cart, name, price, qty=1):
    item = {"name": name, "price": price, "qty": qty}
    cart["items"].append(item)

def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"Error: {e} - Tuples cannot be changed after creation")

def calculate_total(cart):
    subtotal = 0
    for item in cart["items"]:
        subtotal += item["price"] * item["qty"]

    discount_amt = subtotal * (cart["discount"] / 100)
    final_total = subtotal - discount_amt
    return round(final_total, 2)

def main():
    print("=== Customer 1: Rohan ===")
    cart1 = create_cart("Rohan", discount=15)
    add_to_cart(cart1, "Headphones", 2500, 1)
    add_to_cart(cart1, "USB Cable", 299, 3)
    add_to_cart(cart1, "Power Bank", 1200, 1)
    print(f"Cart 1: {cart1['items']}")
    print(f"Total: {calculate_total(cart1)}")

    print("\n=== Customer 2: Sneha ===")
    cart2 = create_cart("Sneha", discount=5)
    add_to_cart(cart2, "Notebook", 80, 4)
    add_to_cart(cart2, "Water Bottle", 350, 1)
    add_to_cart(cart2, "Backpack", 1500, 1)
    print(f"Cart 2: {cart2['items']}")
    print(f"Total: {calculate_total(cart2)}")

    print("\n=== Testing Tuple Immutability ===")
    price_data = (499, "INR")
    update_price(price_data, 599)

    print("\n=== Proving carts are independent ===")
    print(f"Rohan cart items: {len(cart1['items'])}")
    print(f"Sneha cart items: {len(cart2['items'])}")

if __name__ == "__main__":
    main()

