import pytest

from .solution import Solution


class TestSolution:
    
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()
    
    def test_is_anagram(self, solution):
        
        assert solution.is_anagram("anagram", "nagaram") == True
        assert solution.is_anagram("rat", "car") == False   