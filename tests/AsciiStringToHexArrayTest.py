import unittest
from vigenere_cracker import ascii_string_to_hex_array


class AsciiStringToHexArrayTest(unittest.TestCase):
    def test_simple(self):
        expected = ['61', '62', '63']
        actual = ascii_string_to_hex_array('abc')

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
