import unittest


class Hamming:
    def distance(self, value1, value2):
        result = 0
        if (value1 == "" and value2 == "") or (value1 == value2):
            return result
        if len(value1) != len(value2):
            raise ValueError("Genotype lengths should be equal!")
        for i in range(0, len(value1), 1):
            if value1[i] != value2[i]:
                result += 1
        return result


class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        hamming = Hamming()
        self.assertEqual(hamming.distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        hamming = Hamming()
        self.assertEqual(hamming.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        hamming = Hamming()
        self.assertEqual(hamming.distance("G", "T"), 1)

    def test_long_identical_strands(self):
        hamming = Hamming()
        self.assertEqual(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        hamming = Hamming()
        self.assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        hamming = Hamming()
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        hamming = Hamming()
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        hamming = Hamming()
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("", "G")

    def test_disallow_right_empty_strand(self):
        hamming = Hamming()
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("G", "")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
