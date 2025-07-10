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
#   total = 0                                   brute approch
#         for i in range(len(s)):
#             for j in range(i + 1, len(s) + 1):
#                 sub = s[i:j]
#                 freq = {}
#                 for ch in sub:
#                     freq[ch] = freq.get(ch, 0) + 1
#                 total += max(freq.values()) - min(freq.values())
#         return total