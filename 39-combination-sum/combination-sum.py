class Solution:
    # Helper recursive function
    def solve(self, index: int, total: int, subset: List[int], nums: List[int], target: int, result: List[List[int]]):
        # Case 1: Found a valid combination
        if total == target:
            result.append(subset.copy())  # Store a copy of the subset
            return
        
        # Case 2: Exceeded the target
        if total > target or index >= len(nums):
            return
        
        # Include the current number
        subset.append(nums[index])
        self.solve(index, total + nums[index], subset, nums, target, result)  # stay on same index (can reuse)
        
        # Backtrack (remove last added number)
        subset.pop()
        
        # Exclude the current number and move to next index
        self.solve(index + 1, total, subset, nums, target, result)
    
    # Main function
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result