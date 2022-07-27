import pytest

class Solution(object):
    @staticmethod
    def can_attend_meeting(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True



@pytest.mark.parametrize(
    "input, expected",
    [([[0,30],[5,10],[15,20]], False)]
)
def test_permute(input, expected):
    sol = Solution()
    actual = sol.can_attend_meeting(input)
    assert actual == expected
