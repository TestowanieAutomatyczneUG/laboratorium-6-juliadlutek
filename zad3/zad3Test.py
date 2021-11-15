import unittest

with open("./song.txt", "r") as file:
    lines = file.readlines()
    song = file.read()


class Song:
    def returnAllSong(self):
        return song

    def returnOneLine(self, num):
        if num < 1 or type(num) != int:
            raise Exception("Argument should be positive integer!")
        if num == 1:
            line = lines[0].replace("\n", "")
            return line
        if num > 12:
            raise Exception("Argument should be less than or equal to 12")
        else:
            return lines[(2*int(num))-2].replace("\n", "")

    def returnFewLines(self, first, last):
        if first < 1 or last < 1 or type(first) != int or type(last) != int:
            raise Exception("Arguments should be positive integers!")
        if first > last:
            raise Exception("First argument should be less than or equal to second")
        if first > 12 or last > 12:
            raise Exception("Arguments should be less than or equal to 12")
        if first == last:
            return self.returnOneLine(first)
        if first == 1 and last == 12:
            return self.returnAllSong()
        if first == 1:
            return "".join(lines[:((last*2)-1)])
        else:
            return "".join(lines[((first*2)-2):((last*2)-1)])


class SongTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song()

    def test_all_song(self):
        self.assertEqual(self.temp.returnAllSong(), song)

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
        self.assertEqual(self.temp.returnFewLines(1, 12), song)

    def tearDown(self):
        self.temp = None
