# from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
#         maxi = 0

#         for i in range(n):
#             curr_sum = 0
#             for j in range(i, n):
#                 curr_sum += nums[j]
#                 maxi = max(maxi, curr_sum)      time complexity is o(n^2)

#         return maxi



        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum
# time complexity is o(n)