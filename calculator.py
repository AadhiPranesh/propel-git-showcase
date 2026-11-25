def divide(a, b):
    return a / b
    raise ValueError("Cannot divide by zero")

def calculate_discount(price, discount_percent):
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount_percent / 100)