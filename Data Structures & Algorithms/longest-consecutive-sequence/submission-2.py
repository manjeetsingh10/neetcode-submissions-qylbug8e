class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(list(set(nums)))
        res = 1
        for i in range(0, len(nums)):
            ts = 0
            for j in range(i+1, len(nums)):
                if nums[j] - nums[j-1] == 1:
                    ts += 1
                else:
                    break
            res = max(res, ts+1)

        return res