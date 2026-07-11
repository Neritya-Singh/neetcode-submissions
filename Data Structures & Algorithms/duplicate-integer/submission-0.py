class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
        for j in hash_map.values() :
            if j > 1:
                return True
        return False
