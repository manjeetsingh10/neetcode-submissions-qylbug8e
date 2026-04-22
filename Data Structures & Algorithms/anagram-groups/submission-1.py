from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = len(strs)
        result = []
        visited = set()
        for i in range(l):
            compareString = strs[i]
            if compareString in visited:
                continue
            anagramArr = [compareString]
            for j in range(i+1, l):
                if self.isAnagram(compareString, strs[j]) == True:
                    if strs[j] not in visited:
                        visited.add(strs[j])
                    anagramArr.append(strs[j])
            result.append(anagramArr)
        return result
            

        


    def isAnagram(self, f, s):
        c1 = Counter(f)
        c2 = Counter(s)

        if c1 == c2:
            return True
        return False
