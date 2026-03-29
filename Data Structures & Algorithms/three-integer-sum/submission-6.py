class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left + 1 < len(nums) and nums[left] == nums[left + 1]:
                        left += 1
                    left +=1
                    while right > 0 and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return result
