"""
    Provides two_sum function
"""


from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
        Returns a list of lists containing 2 numbers that add up to 3
        PARAMETERS:
        nums (List): An array of numbers
        target (int): Target sum
    """
    return (nums, target)


TEST_NUMS = [2, 7, 11, 15]
TEST_TARGET = 9
ANS = two_sum(TEST_NUMS, TEST_TARGET)

print(ANS)
