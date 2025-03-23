class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=[]
        count=0
        for char in s:
            if char == '(':
                if count > 0:
                    result.append(char)
                count+=1
            else:
                count-=1
                if count > 0:
                    result.append(char)
        return "".join(result)            

# time complexity is o(n)
# space complexity is o(n)