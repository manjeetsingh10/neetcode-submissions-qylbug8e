class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        result = []

        def bt(start, path, currSum):
            if currSum == target:
                result.append(path[:])
            elif currSum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])

                bt(i, path, currSum + nums[i])
                path.pop()

        
        bt(0,[], 0)
        return result