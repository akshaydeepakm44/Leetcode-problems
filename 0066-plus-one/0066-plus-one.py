class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):  # Start from the last digit
            if digits[i] < 9:
                digits[i] += 1  # Increment the digit
                return digits  # Return immediately after incrementing if no carry over
            digits[i] = 0  # Set digit to 0 if it's 9 (carry over)

        # If the loop ends, it means we had a carry over for the most significant digit
        return [1] + digits  # Prepend 1 to the list if there was a carry
