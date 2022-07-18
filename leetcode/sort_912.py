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

        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j - 1] > nums[j]:
                    temp = nums[j - 1]
                    nums[j - 1] = nums[j]
                    nums[j] = temp
        return nums

    @staticmethod
    def insertion_sort(nums):
        for i in range(len(nums)):
            temp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > temp:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp

        return nums

    @staticmethod
    def merge_sort(nums):
        return merge_helper(nums, 0, len(nums) - 1)


def merge_helper(nums, start, end):
    # leaf node:
    if start == end:
        return nums
    # internal node:
    mid = (start + end) // 2
    merge_helper(nums, start, mid)
    merge_helper(nums, mid + 1, end)

    # merge
    i = start
    j = mid + 1
    temp = []
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        elif nums[i] > nums[j]:
            temp.append(nums[j])
            j += 1

    while i <= mid:
        temp.append(nums[i])
        i += 1

    while j <= end:
        temp.append(nums[j])
        j += 1

    count = 0
    for i in range(start, end + 1, 1):
        nums[i] = temp[count]
        count += 1
    return nums


@pytest.mark.parametrize(
    "input, expected",
    [
        ([5, 2, 3, 1], [1, 2, 3, 5]),
        ([0], [0])
    ]
)
class TestSort:
    sol = Solution()

    def test_selection_sort(self,input, expected):
        actual = self.sol.selection_sort(nums=input)
        assert actual == expected

    def test_bubble_sort(self, input, expected):
        actual = self.sol.bubble_sort(nums=input)
        assert actual == expected

    def test_insertion_sort(self, input, expected):
        actual = self.sol.insertion_sort(nums=input)
        assert actual == expected

    def test_merge_sort(self, input, expected):
        actual = self.sol.merge_sort(nums=input)
        assert actual == expected
