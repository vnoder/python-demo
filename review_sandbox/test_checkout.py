import unittest

from checkout import CartItem, Quote, quote_order


class QuoteOrderTests(unittest.TestCase):
    def test_single_item_below_shipping_threshold(self):
        self.assertEqual(quote_order([CartItem(2_000, 1)]), Quote(2_000, 0, 500, 2_500))

    def test_every_unit_is_charged(self):
        self.assertEqual(quote_order([CartItem(2_000, 3)]), Quote(6_000, 0, 500, 6_500))

    def test_discount_reduces_total(self):
        self.assertEqual(
            quote_order([CartItem(5_000, 1)], discount_cents=1_000),
            Quote(5_000, 1_000, 500, 4_500),
        )

    def test_free_shipping_includes_exact_threshold(self):
        self.assertEqual(quote_order([CartItem(10_000, 1)]), Quote(10_000, 0, 0, 10_000))

    def test_discount_applies_before_shipping_threshold(self):
        self.assertEqual(
            quote_order([CartItem(10_500, 1)], discount_cents=1_000),
            Quote(10_500, 1_000, 500, 10_000),
        )

    def test_empty_cart_is_rejected(self):
        with self.assertRaises(ValueError):
            quote_order([])

    def test_negative_discount_is_rejected(self):
        with self.assertRaises(ValueError):
            quote_order([CartItem(2_000, 1)], discount_cents=-1)


if __name__ == "__main__":
    unittest.main()
