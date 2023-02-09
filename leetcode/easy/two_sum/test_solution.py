import pytest

from .solution import Solution


class TestSolution:
    
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()
    
    def test_two_sum(self, solution):
        assert solution.two_sum([2, 7, 11, 15], 9) == [0,1]
        assert solution.two_sum([3,2,4], 6) == [1,2]
        assert solution.two_sum([3,3], 6) == [0,1]
