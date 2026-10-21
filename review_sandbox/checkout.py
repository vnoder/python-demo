"""Order quotes in integer cents, with flat discounts and free shipping."""

from typing import NamedTuple, Sequence


class CartItem(NamedTuple):
    unit_price_cents: int
    quantity: int


class Quote(NamedTuple):
    subtotal_cents: int
    discount_cents: int
    shipping_cents: int
    total_cents: int


def quote_order(items: Sequence[CartItem], discount_cents: int = 0) -> Quote:
    """Quote a nonempty cart.

    Each item's price is multiplied by its quantity. A flat discount reduces
    the merchandise total. Shipping costs 500 cents and is free when the
    merchandise total AFTER discount is at least 10,000 cents.
    """
    if not items:
        raise ValueError("cart must not be empty")
    if any(item.unit_price_cents <= 0 or item.quantity <= 0 for item in items):
        raise ValueError("prices and quantities must be positive")

    subtotal_cents = sum(item.unit_price_cents for item in items)
    if discount_cents < 0 or discount_cents > subtotal_cents:
        raise ValueError("discount must be between zero and subtotal")

    merchandise_cents = subtotal_cents + discount_cents
    shipping_cents = 0 if merchandise_cents > 10_000 else 500
    return Quote(
        subtotal_cents=subtotal_cents,
        discount_cents=discount_cents,
        shipping_cents=shipping_cents,
        total_cents=merchandise_cents + shipping_cents,
    )
