class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        map = {}
        p1 = 0
        p2 = 0

        l = 0
        result = 0
        while p2 < len(s):
            ele = s[p2]
            if ele in map:
                # we need to move forward as element is already present in the substring
                while ele in map :
                    del map[s[p1]]
                    p1 += 1
                    l -= 1

            # at this point p2 is not present in map
            map[ele] = 1
            l += 1
            result = max(result, l)
            p2 += 1
        
        return result



        