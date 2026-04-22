class Solution:

    def encode(self, strs: List[str]) -> str:
        message = str()
        for s in strs:
            message += str(len(s)) + "#" + s
        return message

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        l = len(s)
        while i < l:
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])

            i = j + 1
            j += length

            extractedWord = s[i:j+1]
            res.append(extractedWord)
            i = j + 1

        return res
            