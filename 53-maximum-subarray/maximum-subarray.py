import sys
class Solution:
    def maxSubArray(self, nums: List[int])-> int:
        maxsum= float('-inf')
        currentsum=0

        for n in nums:
            currentsum += n

            if currentsum> maxsum:
                maxsum= currentsum

            #reset val to 0
        
            if currentsum<0:
                currentsum=0
        return maxsum
        