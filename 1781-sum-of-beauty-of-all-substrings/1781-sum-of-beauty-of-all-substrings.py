class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range (len(s)):
            freq = Counter()
            for j in range(i,len(s)):
                freq [s[j]] += 1
                values  = freq.values()
                total += max(values) - min(values)
        return total 
 