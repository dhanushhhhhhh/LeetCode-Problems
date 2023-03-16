class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numeral = ""
        thousands = num // 1000
        roman_numeral += "M"*thousands

        hundreds = (num % 1000) // 100
        if hundreds == 9:
            roman_numeral += "CM"
        elif hundreds == 4:
            roman_numeral += "CD"
        elif hundreds == 5:
            roman_numeral += "D"
        elif hundreds > 5:
            roman_numeral += "D"
            roman_numeral += (hundreds - 5) * "C"
        else:
            roman_numeral += "C"*hundreds

        tens = (num % 100) // 10
        if tens == 9:
            roman_numeral += "XC"
        elif tens == 4:
            roman_numeral += "XL"
        elif tens == 5:
            roman_numeral += "L"
        elif tens > 5:
            roman_numeral += "L"
            roman_numeral += (tens - 5) * "X"
        else:
            roman_numeral += "X"*tens

        ones = (num % 10)
        if ones == 9:
            roman_numeral += "IX"
        elif ones == 4:
            roman_numeral += "IV"
        elif ones == 5:
            roman_numeral += "V"
        elif ones > 5:
            roman_numeral += "V"
            roman_numeral += (ones - 5) * "I"
        else:
            roman_numeral += "I"*ones

        return roman_numeral
