class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = [0]*26
        hash_t = [0]*26
        for i in s:
            ascii_val = ord(i) - 97
            hash_s[ascii_val] += 1
        for j in t:
            ascii_val = ord(j) - 97
            hash_t[ascii_val] += 1

        if hash_s == hash_t :
            return True
        else :
            return False