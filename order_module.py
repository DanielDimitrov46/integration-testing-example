# order_module.py

from product_module import get_product
from discount_module import apply_discount

def calculate_total_price(order_items):
    total = 0
    for product_id, quantity in order_items:
        product = get_product(product_id)
        if product:
            total += product["price"] * quantity
    return apply_discount(total)