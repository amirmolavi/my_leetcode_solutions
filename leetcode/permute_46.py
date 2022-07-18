import pytest


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []

        # base case:
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            output.extend(perms)
            nums.append(n)

        return output


@pytest.mark.parametrize(
    "input, expected",
    [([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])]
)
def test_permute(input, expected):
    sol = Solution()
    actual = sol.permute(nums=input)
    assert sorted(actual) == sorted(expected)
