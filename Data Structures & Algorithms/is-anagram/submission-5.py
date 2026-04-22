from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            freq = Counter(s)
            freq2 = Counter(t)

            if freq == freq2:
                return True
            return False




        