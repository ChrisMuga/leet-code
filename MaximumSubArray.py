from typing import List


# Given an array the algorithm to find the maximum sub-array sum, is called: Kadane's algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = current_sum = float('-inf')
        current_sum = best_sum

        for num in nums:
            current_sum = max(current_sum + num, num)
            best_sum = max(current_sum, best_sum)
        return best_sum


solution = Solution()
input_values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = solution.maxSubArray(input_values)
print(ans)
