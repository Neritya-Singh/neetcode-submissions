class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs :
            if "".join(sorted(i)) not in hash_map :
                hash_map["".join(sorted(i))] = [i]
            else :
                hash_map["".join(sorted(i))].append(i)
        
        output = []

        for j in hash_map.values() :
            output.append(j)

        return output
