class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(e for e in s if e.isalnum()).lower()
        
        # Compare the string with its reverse
        return s == s[::-1]
