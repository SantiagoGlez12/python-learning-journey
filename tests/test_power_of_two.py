import unittest
from fundamentals.power_of_two import es_potencia_de_2


class TestPowerOfTwo(unittest.TestCase):
    def test_powers(self):
        for number in (1, 2, 4, 8, 16, 1024):
            self.assertTrue(es_potencia_de_2(number))

    def test_non_powers(self):
        for number in (0, 3, 7, 10, 100000, -2, True, 4.0):
            self.assertFalse(es_potencia_de_2(number))


if __name__ == "__main__":
    unittest.main()
