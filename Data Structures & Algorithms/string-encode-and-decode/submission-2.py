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
            # print("s ", s)
            # print("i ", i)
            # print("j ", j)
            length = int(s[i:j])
            # print("extracted length ", length)

            i = j + 1
            j += length

            extractedWord = s[i:j+1]
            # print("extracted word ", extractedWord)
            res.append(extractedWord)
            i = j + 1

        return res
            