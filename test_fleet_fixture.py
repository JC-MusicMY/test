import unittest

from fleet_fixture import clamp


class ClampTests(unittest.TestCase):
    def test_value_below_lower_returns_lower(self):
        self.assertEqual(clamp(-1, 0, 10), 0)

    def test_value_above_upper_returns_upper(self):
        self.assertEqual(clamp(11, 0, 10), 10)

    def test_value_inside_bounds_is_unchanged(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_bounds_are_inclusive(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_equal_bounds(self):
        self.assertEqual(clamp(-100, 7, 7), 7)
        self.assertEqual(clamp(100, 7, 7), 7)

    def test_reversed_bounds_raise_value_error(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


if __name__ == "__main__":
    unittest.main()
