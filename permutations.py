# pylint: skip-file
from typing import List


class Solution:
    def permute(self, nums: List[int])->List[List[int]]:
        result = []
        for idx, num in enumerate(nums):
            for idx_, num_ in enumerate(nums):
                copy_ = nums.copy()
                if idx != idx_:
                    copy_[idx_] = num
                    copy_[idx] = num_
                    result.append(copy_)
            break

        return(result)


solution = Solution()


input_nums = [1, 2, 3]
ans = solution.permute(input_nums)
print(ans)
