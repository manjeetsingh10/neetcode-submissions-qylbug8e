# approach 1
# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

# approach 2
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
            if len(s) != len(t):
                return False
            count = {}
            for c in s:
                count[c] = count.get(c, 0) + 1
            for c in t:
                count[c] = count.get(c, 0) - 1
                if (count[c] == -1):
                    return False
            return True