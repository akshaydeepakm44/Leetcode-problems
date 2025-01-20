import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        
        divisors_sum = 1  # Start with 1 because 1 is always a divisor (excluding num itself)
        
        # Check divisors up to sqrt(num)
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors_sum += i
                # Add the corresponding paired divisor if it's different
                if i != num // i:
                    divisors_sum += num // i
        
        return divisors_sum == num
