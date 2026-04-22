class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        # Case 1: more than one zero
        if zero_count > 1:
            return [0] * len(nums)

        # product of non-zero elements
        product = 1
        for num in nums:
            if num != 0:
                product *= num

        result = []

        for num in nums:
            if zero_count == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // num)

        return result