from collections import deque
from typing import List

class Solution:
    def ladderLength(self, startWord: str, targetWord: str, wordList: List[str]) -> int:
        if (targetWord not in wordList) or (startWord == targetWord):
            return 0

        totalWords = len(wordList)
        wordLength = len(wordList[0])

        adjacencyList = [[] for _ in range(totalWords)]
        wordToIndexMap = {}

        # Map each word to its index
        for index in range(totalWords):
            wordToIndexMap[wordList[index]] = index

        # Build graph (connect words differing by 1 character)
        for i in range(totalWords):
            for j in range(i + 1, totalWords):
                diffCount = 0
                for k in range(wordLength):
                    if wordList[i][k] != wordList[j][k]:
                        diffCount += 1
                if diffCount == 1:
                    adjacencyList[i].append(j)
                    adjacencyList[j].append(i)

        queue = deque()
        transformationLength = 1
        visitedIndices = set()

        # Initialize BFS with words 1 step away from startWord
        for pos in range(wordLength):
            for charCode in range(97, 123):  # a-z
                newChar = chr(charCode)
                if newChar == startWord[pos]:
                    continue

                transformedWord = startWord[:pos] + newChar + startWord[pos + 1:]

                if transformedWord in wordToIndexMap:
                    wordIndex = wordToIndexMap[transformedWord]
                    if wordIndex not in visitedIndices:
                        queue.append(wordIndex)
                        visitedIndices.add(wordIndex)

        # BFS traversal
        while queue:
            transformationLength += 1

            for _ in range(len(queue)):
                currentIndex = queue.popleft()

                if wordList[currentIndex] == targetWord:
                    return transformationLength

                for neighborIndex in adjacencyList[currentIndex]:
                    if neighborIndex not in visitedIndices:
                        visitedIndices.add(neighborIndex)
                        queue.append(neighborIndex)

        return 0