import unittest
from lbtt_calc import calculate_basic_lbtt

# test class for testing the ranges of values accepted by the tax calculation function

# note, the program is usually started via main, ensuring the input is validated
# but since the function is being tested directly, we also ensure the function can
# raise errors on invalid values
class TestTax(unittest.TestCase):
    # these tests only test positive input values
    # negative inputs can be recieved and will return 0 but they shouldn't be accepted
    def test_tax(self):
        self.assertAlmostEqual(calculate_basic_lbtt(0), 0)
        self.assertAlmostEqual(calculate_basic_lbtt(1), 0)
        self.assertAlmostEqual(calculate_basic_lbtt(250000.01), 0)
        self.assertAlmostEqual(calculate_basic_lbtt(250000.5), 0.03)
        self.assertAlmostEqual(calculate_basic_lbtt(250001), 0.05)
        self.assertAlmostEqual(calculate_basic_lbtt(250040), 2)
        self.assertAlmostEqual(calculate_basic_lbtt(239493), 0)
        self.assertAlmostEqual(calculate_basic_lbtt(290500), 2025)
        self.assertAlmostEqual(calculate_basic_lbtt(322500), 3625)
        self.assertAlmostEqual(calculate_basic_lbtt(387000), 9950)
        self.assertAlmostEqual(calculate_basic_lbtt(500000), 21250)
        self.assertAlmostEqual(calculate_basic_lbtt(745000), 45750)
        self.assertAlmostEqual(calculate_basic_lbtt(775000), 49250)
        self.assertAlmostEqual(calculate_basic_lbtt(900000), 64250)
        self.assertAlmostEqual(calculate_basic_lbtt(1200000), 100250)
        self.assertAlmostEqual(calculate_basic_lbtt(10000000), 1156250)
    
    # test values that are invalid are not allowed to cause unexpected errors
    def test_input_val(self):
        with self.assertRaises(TypeError): calculate_basic_lbtt("Bob")
        with self.assertRaises(TypeError): calculate_basic_lbtt("Bob543")
        with self.assertRaises(ValueError): calculate_basic_lbtt(-1)

if __name__ == "__main__":
    unittest.main()