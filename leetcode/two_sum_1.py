import pytest


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, val in enumerate(nums):
            new_target = target - val
            for j in range(i + 1, len(nums), 1):
                if nums[j] == new_target:
                    return [i, j]

    @staticmethod
    def two_sum_o_n(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}
        for i, val in enumerate(nums):
            new_target = target - val
            if new_target in map:
                return [i, map[new_target]]
            else:
                map[val] = i


@pytest.mark.parametrize(
    "input, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2])
    ]
)
class TestTwoSum:
    def test_two_sum(self, input, target, expected):
        sol = Solution()
        actual = sol.two_sum(nums=input, target=target)
        assert sorted(actual) == sorted(expected)

    def test_two_sum_o_n(self, input, target, expected):
        sol = Solution()
        actual = sol.two_sum_o_n(nums=input, target=target)
        assert sorted(actual) == sorted(expected)
