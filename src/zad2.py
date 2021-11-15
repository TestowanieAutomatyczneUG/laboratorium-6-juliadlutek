
def roman(number):
    if number >= 1000:
        return str("M" + roman(number-1000))
    elif number >= 900:
        return str("CM" + roman(number-900))
    elif number >= 500:
        return str("D" + roman(number-500))
    elif number >= 400:
        return str("CD"+roman(number-400))
    elif number >= 100:
        return str("C"+roman(number-100))
    elif number >= 90:
        return str("XC"+roman(number-90))
    elif number >= 50:
        return str("L"+roman(number-50))
    elif number >= 40:
        return str("XL"+roman(number-40))
    elif number >= 10:
        return str("X" + roman(number-10))
    elif number == 9:
        return "IX"
    elif number >= 5:
        return str("V"+roman(number-5))
    elif number == 4:
        return "IV"
    elif number <= 3:
        return str(number*"I")
    elif number == 0:
        return
    else:
        return ValueError("Number should be positive!")
