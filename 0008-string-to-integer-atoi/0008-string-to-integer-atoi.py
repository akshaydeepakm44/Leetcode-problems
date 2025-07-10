class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing spaces
        if not s:
            return 0
        
        sign = 1
        index = 0
        result = 0
        int_max = 2**31 - 1
        int_min = -2**31

        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1

        result *= sign

        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result
