class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        diff = 15000 # max diff = 13000
            
        for i in range(len(nums) - 2):
            #if(i == 0 or (i > 0 and nums[i] != nums[i - 1])):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if abs(nums[i] + nums[left] + nums[right] - target) < diff:
                    ans = nums[i] + nums[left] + nums[right]
                    diff = abs(nums[i] + nums[left] + nums[right] - target)
                elif nums[i] + nums[left] + nums[right] - target < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] - target > 0:
                    right -= 1
                else:
                    return ans
        return ans
