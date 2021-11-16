
with open("/home/runner/work/laboratorium-6-juliadlutek/laboratorium-6-juliadlutek/src/zad3/song.txt", "r") as file:
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
