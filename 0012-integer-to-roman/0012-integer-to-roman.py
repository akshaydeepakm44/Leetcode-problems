class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the Roman numerals and their corresponding values
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        # Initialize the result string
        result = ""
        
        # Iterate over the Roman numeral values
        for value, symbol in roman_numerals:
            # While the number is larger than or equal to the current value
            while num >= value:
                result += symbol  # Append the Roman symbol
                num -= value      # Subtract the value from the number
        
        return result
