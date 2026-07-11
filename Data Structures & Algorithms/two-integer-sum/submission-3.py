class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #this will be better solution.
        hash_map = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hash_map :
                return sorted([hash_map.get(remaining),i])
                
            else :
                hash_map[nums[i]] = i