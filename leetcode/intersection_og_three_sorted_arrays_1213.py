import pytest


class Solution(object):
    def arrays_intersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = 0
        p3 = 0
        arr = []

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
                arr.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            elif arr1[p1] < arr2[p2] or arr1[p1] < arr3[p3]:
                p1 += 1
            elif arr2[p2] < arr1[p1] or arr2[p2] < arr3[p3]:
                p2 += 1
            elif arr3[p3] < arr1[p1] or arr3[p3] < arr2[p2]:
                p3 += 1
        return arr


@pytest.mark.parametrize(
    "arr1, arr2, arr3, expected",
    [([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8], [1, 5])]
)
def test_permute(arr1, arr2, arr3, expected):
    sol = Solution()
    actual = sol.arrays_intersection(arr1, arr2, arr3)
    assert actual == expected
