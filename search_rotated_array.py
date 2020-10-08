# pylint:skip-file
from typing import List


class Solution:
    def search(self, nums: List[int], target: int):
        for idx, num in enumerate(nums):
            if num == target:
                return idx
        return -1


solution = Solution()


input_nums = [4, 5, 6, 7, 0, 1, 2]
input_target = 0

ans = solution.search(input_nums, input_target)
print(ans)
