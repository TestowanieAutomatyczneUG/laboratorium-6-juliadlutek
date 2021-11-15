import unittest
import src.zad3.zad3 as zad3

class SongTest(unittest.TestCase):
    def setUp(self):
        self.temp = zad3.Song()

    def test_all_song(self):
        self.assertEqual(self.temp.returnAllSong(), zad3.song)

    def test_first_line(self):
        self.assertEqual(self.temp.returnOneLine(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_tenth_line(self):
        self.assertEqual(self.temp.returnOneLine(10), "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_one_line_negative_value(self):
        self.assertRaises( Exception, self.temp.returnOneLine, -1)

    def test_one_line_too_big_value(self):
        self.assertRaises( Exception, self.temp.returnOneLine, 13)

    def test_few_lines_negative_value(self):
        self.assertRaises(Exception, self.temp.returnFewLines, -4, 12)

    def test_few_lines_too_big_value(self):
        self.assertRaises(Exception, self.temp.returnFewLines, 1, 20)

    def test_first_grater_than_last(self):
        self.assertRaises(Exception, self.temp.returnFewLines, 4, 1)

    def test_second_to_third_line(self):
        self.assertMultiLineEqual(self.temp.returnFewLines(2, 3), ("On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n" + "\n" + "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n"))

    def test_few_lines_equal_values(self):
        self.assertEqual(self.temp.returnFewLines(4, 4), "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_first_to_twelth_line(self):
        self.assertEqual(self.temp.returnFewLines(1, 12), zad3.song)

    def tearDown(self):
        self.temp = None
