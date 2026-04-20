class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(index, current_subset):
            # 1. Base Case: We've made a decision for every number
            if index == len(nums):
                # We append a COPY of the subset, otherwise it mutates later
                result.append(current_subset[:]) 
                return
            
            # --- DECISION 1: Include nums[index] ---
            current_subset.append(nums[index])
            backtrack(index + 1, current_subset)
            
            # --- DECISION 2: Exclude nums[index] (The Backtrack!) ---
            current_subset.pop()
            backtrack(index + 1, current_subset)
            
        backtrack(0, [])
        return result
        