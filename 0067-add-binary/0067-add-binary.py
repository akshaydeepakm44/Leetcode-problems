class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
    
        sum = a + b
        
        # Convert the sum back to binary and remove the "0b" prefix
        return bin(sum)[2:]
