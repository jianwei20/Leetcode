class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def bs(arr, target, left, right):
            m = (left + right) // 2
            
            if left == right and arr[m] != target:
                if arr[m] > target:
                    return m
                elif arr[m] < target:
                    return m + 1
            elif arr[m] == target:
                return m
            
            elif arr[m] > target:
                return bs(arr, target, left, m)
                
            elif arr[m] < target:
                return bs(arr, target, m + 1, right)
        
        return bs(nums, target, 0, len(nums) - 1)
