class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31        
        INT_MAX = 2**31 - 1     
        
        negative = x < 0
        x = abs(x)
        result = 0

        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10

        if negative:
            result = -result

        # Check for 32-bit overflow
        if result < INT_MIN or result > INT_MAX:
            return 0

        return result
