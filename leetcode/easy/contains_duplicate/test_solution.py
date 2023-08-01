import pytest

from ..group_anagrams.solution import Solution


class TestSolution:
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()

    def test_contains_duplicate(self, solution):
        assert solution.contains_duplicate([1, 2, 1]) == True
        assert solution.contains_duplicate([1, 2, 3]) == False
        assert solution.contains_duplicate([1]) == False
