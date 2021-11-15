
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

