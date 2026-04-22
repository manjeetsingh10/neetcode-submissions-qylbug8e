class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            ele = nums[i]
            t = target - ele
            for j in range(i+1, l):
                if nums[j] == t:
                    return [i, j]