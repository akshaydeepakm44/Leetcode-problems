class Solution:
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        first_occurrence = {}  
        for i, char in enumerate(s):  
            if char in first_occurrence: 
                return char  
            else:
                first_occurrence[char] = i  