class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compute count with first string
        if not s or not t:
            return False
        count = {}
        string_to_iterate_first = s
        string_to_iterate_second = t

        if len(t) > len(s):
            string_to_iterate_first = t
            string_to_iterate_second = s
        for character in string_to_iterate_first:
            if character in count:
                count[character] = count[character] + 1
            else:
                count[character] = 1
        count_keys = count.keys()
        for character in string_to_iterate_second:
            if character in count_keys:
                count[character] = count[character] - 1
                if (count[character] == 0):
                    del count[character]
        
        if len(count.keys()) == 0:
            return True
        return False
        
