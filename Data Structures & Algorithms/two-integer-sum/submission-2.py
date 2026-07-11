class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in nums :
                j = nums.index(remaining)
                if i != j :
                    return sorted([i,j])
