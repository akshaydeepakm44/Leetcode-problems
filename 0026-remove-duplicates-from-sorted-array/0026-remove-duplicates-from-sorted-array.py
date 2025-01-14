class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize the pointer for placing unique elements
        i = 1
        
        # Iterate through the list starting from the second element
        for j in range(1, len(nums)):
            # Check if the current element is different from the last unique element
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        
        return i
