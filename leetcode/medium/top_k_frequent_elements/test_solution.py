
import pytest

from .solution import Solution


class TestSolution:
    
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()
    
    def test_top_k_frequent_elements(self, solution):
    
        assert solution.top_k_frequent_elements([1,1,1,2,2,3], 2) == [1, 2]
        assert solution.top_k_frequent_elements([1], 1) == [1]
