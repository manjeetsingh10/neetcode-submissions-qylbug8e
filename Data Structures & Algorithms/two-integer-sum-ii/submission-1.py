class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            e1 = numbers[p1]
            e2 = numbers[p2]
            s = e1 + e2

            if s == target:
                return [p1 + 1, p2 + 1]
            
            if s > target:
                p2 -= 1
            elif s < target:
                p1 += 1
        return [-1, -1]

        