class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map.values():
                # If it's an opening bracket, push it to the stack
                stack.append(char)
            elif char in bracket_map:
                # If it's a closing bracket, check if the stack is empty or top of the stack doesn't match
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Pop the matched opening bracket
            else:
                # Invalid character (though the problem guarantees valid input, this is a safeguard)
                return False
        
        # If the stack is empty, all brackets matched; otherwise, it's invalid
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))       # Output: True
print(solution.isValid("()[]{}"))   # Output: True
print(solution.isValid("(]"))       # Output: False
print(solution.isValid("([])"))     # Output: True
