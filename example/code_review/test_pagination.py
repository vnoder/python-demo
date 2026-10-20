import unittest

from pagination import paginate


class PaginationTest(unittest.TestCase):
    def test_first_middle_and_last_page(self):
        items = [1, 2, 3, 4, 5]
        self.assertEqual(paginate(items, page=1, page_size=2), [1, 2])
        self.assertEqual(paginate(items, page=2, page_size=2), [3, 4])
        self.assertEqual(paginate(items, page=3, page_size=2), [5])

    def test_empty_and_out_of_range_pages(self):
        self.assertEqual(paginate([]), [])
        self.assertEqual(paginate([1, 2], page=2, page_size=2), [])

    def test_returns_an_independent_list(self):
        items = [1, 2, 3]
        result = paginate(items)
        result.append(4)
        self.assertEqual(items, [1, 2, 3])
        self.assertEqual(paginate((1, 2, 3)), [1, 2, 3])

    def test_rejects_nonpositive_page_parameters(self):
        for name in ("page", "page_size"):
            for value in (0, -1):
                with self.subTest(name=name, value=value):
                    with self.assertRaises(ValueError):
                        paginate([1], **{name: value})

    def test_rejects_noninteger_page_parameters(self):
        for name in ("page", "page_size"):
            for value in (True, False, 1.5, "2", None):
                with self.subTest(name=name, value=value):
                    with self.assertRaises(TypeError):
                        paginate([1], **{name: value})


if __name__ == "__main__":
    unittest.main()
