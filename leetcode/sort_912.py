import pytest


class Solution(object):
    @staticmethod
    def selection_sort(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i, n in enumerate(nums):
            min_val = n
            min_ind = i
            for j in range(i + 1, len(nums), 1):
                if nums[j] < min_val:
                    min_val = nums[j]
                    min_ind = j

            temp = nums[i]
            nums[i] = nums[min_ind]
            nums[min_ind] = temp

        return nums

    @staticmethod
    def bubble_sort(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                if nums[j - 1] > nums[j]:
                    temp = nums[j - 1]
                    nums[j - 1] = nums[j]
                    nums[j] = temp
        return nums

    @staticmethod
    def insertion_sort(nums):
        pass




@pytest.mark.parametrize(
    "input, expected",
    [([5, 2, 3, 1], [1, 2, 3, 5])]
)
def test_permute(input, expected):
    sol = Solution()
    actual = sol.bubble_sort(nums=input)
    assert sorted(actual) == sorted(expected)
