class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        
        count = nums.count(0)
        print("count ", count)
        p = 1
        for ele in nums:
            p = p * ele
        
        result = [p for i in range(len(nums))]


        for i in range(len(nums)):
            if count == 1 and nums[i] == 0:
                p = 1
                for j in range(len(nums)):
                    if j == i:
                        continue
                    p = p * nums[j]
                result[i] = p
                continue
            if nums[i] != 0:
                result[i] = int(result[i]/nums[i])
            
        return result
        