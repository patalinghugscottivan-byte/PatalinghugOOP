"""discounts.py - discount rules"""

BULK_DISCOUNT_THRESHOLD = 500.00  # orders worth this much or more get a discount
BULK_DISCOUNT_RATE = 0.10         # 10% bulk discount
SENIOR_PWD_RATE = 0.20            # 20% senior citizen / PWD discount


def apply_discount(subtotal, is_senior_pwd):
    """Return (label, amount) of the best available discount."""
    discount_label = "None"
    discount_amount = 0.00

    if subtotal >= BULK_DISCOUNT_THRESHOLD:
        discount_label = "Bulk Order Discount (10%)"
        discount_amount = subtotal * BULK_DISCOUNT_RATE

    if is_senior_pwd:
        senior_amount = subtotal * SENIOR_PWD_RATE
        if senior_amount > discount_amount:
            discount_label = "Senior/PWD Discount (20%)"
            discount_amount = senior_amount

    return discount_label, discount_amount