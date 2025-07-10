class Solution:
    def romanToInt(self, s: str) -> int:
        # Step 1: Map of Roman numerals
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0  # Final result
        
        # Step 2: Loop through the string
        for i in range(len(s)):
            value = roman[s[i]]  # Current Roman character's value
            
            # Step 3: Check if next character is larger (subtraction case)
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= value
            else:
                total += value
        
        return total
