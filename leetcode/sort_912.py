import pytest
import random


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

            nums[i], nums[min_ind] = nums[min_ind], nums[i]

        return nums

    @staticmethod
    def bubble_sort(nums):
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
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

    @staticmethod
    def quick_sort_lumoto(nums):
        return quick_sort_lumoto_helper(nums, 0, len(nums) - 1)

    @staticmethod
    def quick_sort_hoare(nums):
        return quick_sort_hoare_helper(nums, 0, len(nums) - 1)


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


def quick_sort_lumoto_helper(nums, start, end):
    # leaf node:
    if start >= end:
        return nums

    # internal node worker
    random.seed(0)
    rand = random.randrange(start, end)
    nums[start], nums[rand] = nums[rand], nums[start]

    # Lumoto's partitioning
    smaller = start

    for bigger in range(start + 1, end + 1, 1):
        if nums[bigger] < nums[start]:
            smaller += 1
            nums[smaller], nums[bigger] = nums[bigger], nums[smaller]

    nums[start], nums[smaller] = nums[smaller], nums[start]

    quick_sort_lumoto_helper(nums, start, smaller - 1)
    quick_sort_lumoto_helper(nums, smaller + 1, end)

    return nums


def quick_sort_hoare_helper(nums, start, end):
    # leaf node:
    if start >= end:
        return nums

    # internal node worker
    random.seed(0)
    rand = random.randrange(start, end)
    nums[start], nums[rand] = nums[rand], nums[start]

    # Lumoto's partitioning
    smaller = start + 1
    bigger = end

    while smaller <= bigger:
        if nums[smaller] < nums[start]:
            smaller += 1
        elif nums[bigger] > nums[start]:
            bigger -= 1
        else:
            nums[smaller], nums[bigger] = nums[bigger], nums[smaller]
            smaller += 1
            bigger -= 1

    nums[start], nums[bigger] = nums[bigger], nums[start]

    quick_sort_lumoto_helper(nums, start, bigger - 1)
    quick_sort_lumoto_helper(nums, bigger + 1, end)

    return nums


@pytest.mark.parametrize(
    "input, expected",
    [
        ([5, 2, 3, 1], [1, 2, 3, 5]),
        ([0], [0]),
        ([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1], [-7, -5, -4, -1, -1, 0, 0, 4, 7, 9]),
    ]
)
class TestSort:
    sol = Solution()

    def test_selection_sort(self, input, expected):
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

    def test_quick_sort_lumoto(self, input, expected):
        actual = self.sol.quick_sort_lumoto(nums=input)
        assert actual == expected

    def test_quick_sort_hoare(self, input, expected):
        actual = self.sol.quick_sort_hoare(nums=input)
        assert actual == expected
