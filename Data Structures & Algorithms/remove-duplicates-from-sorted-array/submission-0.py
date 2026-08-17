class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash = {}
        for i in nums :
            hash[i] = hash.get(i,0) + 1

        unique = list(hash.keys())

        nums[:len(unique)] = unique

        return len(unique)