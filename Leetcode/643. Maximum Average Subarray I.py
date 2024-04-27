"""
643. Maximum Average Subarray I
"""

# Solved using sliding window technique
# Create a sum till the target index, and loop the aray from that point. Note the left pointer index is nothing but i - k, k is a constant and i in the iteration, so the left pointer moves like 0, 1, 2, 3 .....

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i - k]

            maxSum = max(maxSum, curSum)

        return maxSum / k
