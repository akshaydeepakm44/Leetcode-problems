class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {} 
        ts = {}  
        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            
            if c1 in st:
                if st[c1] != c2:  
                    return False
            elif c2 in ts:
                if ts[c2] != c1:  
                    return False
            else:
                st[c1] = c2 
                ts[c2] = c1 
        
        return True