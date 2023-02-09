import pytest

from .solution import Solution


class TestSolution:
    
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()
    
    def test_contains_duplicate(self, solution):
        assert solution.contains_duplicate([1, 2, 3, 1]) == True
        assert solution.contains_duplicate([1, 2, 3, 4]) == False
        assert solution.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
