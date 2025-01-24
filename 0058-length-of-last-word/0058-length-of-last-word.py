class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        
        # The last word is the last element in the list
        return len(words[-1]) if words else 0
