class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            print("false")
            return False
        
        a = x  
        b = int(str(x)[::-1])  
        
        if a == b:
            print("true")
            return True
        else:
            print("false")
            return False