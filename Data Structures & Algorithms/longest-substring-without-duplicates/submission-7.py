class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        lookup = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            if not lookup.get(char):
                lookup[char] = 1
            else:
                # remove the keys
                while lookup.get(char) > 0 and left < right:
                    lookup[s[left]] -= 1
                    left += 1
                lookup[char] = 1
            max_length = max(max_length, right - left + 1)
        return max_length

