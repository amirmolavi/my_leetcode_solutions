import pytest


class Solution(object):
    def __init__(self, nums1, m, nums2, n):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n
    def merge_my_version(self):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        mm = 0
        nn = 0
        m_end_pointer = self.m - 1

        while mm <= m_end_pointer and nn < self.n:
            if self.nums1[mm] < self.nums2[nn]:
                mm += 1
            elif self.nums1[mm] >= self.nums2[nn]:
                new_mm = m_end_pointer
                while new_mm >= mm:
                    self.nums1[new_mm + 1] = self.nums1[new_mm]
                    new_mm -= 1
                self.nums1[mm] = self.nums2[nn]
                mm += 1
                nn += 1
                m_end_pointer += 1
        if nn < self.n:
            while nn < self.n:
                self.nums1[mm] = self.nums2[nn]
                mm += 1
                nn += 1

    def merge(self):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        last = self.n + self.m - 1
        self.m = self.m - 1
        self.n = self.n - 1

        while self.m >= 0 and self.n >= 0:
            if self.nums1[self.m] >= self.nums2[self.n]:
                self.nums1[last] = self.nums1[self.m]
                self.m -= 1
            else:
                self.nums1[last] = self.nums2[self.n]
                self.n -= 1
            last -= 1

        if self.n >= 0:
            while self.n >= 0:
                self.nums1[last] = self.nums2[self.n]
                self.n -= 1
                last -= 1

@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [([1,2,3,0,0,0], 3, [2, 5, 6], 3, [1,2,2,3,5,6])]
)
def test_permute(nums1, m, nums2, n, expected):
    sol = Solution(nums1, m, nums2, n)
    sol.merge()
    actual = sol.nums1
    assert actual == expected