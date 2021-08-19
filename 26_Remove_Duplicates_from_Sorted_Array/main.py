class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        counts = 1
        for i in range(1, len(nums)):
            if nums[counts - 1] < nums[i]:
                nums[counts] = nums[i]
                counts += 1
        return counts
                
