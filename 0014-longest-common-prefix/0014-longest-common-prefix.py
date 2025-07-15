class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):           
            char = strs[0][i]                   # Take the i-th character as reference
            for other in strs[1:]:              # Compare with every other string
                if i >= len(other) or other[i] != char:
                    return strs[0][:i]          # Return the prefix found so far
        return strs[0]                         
