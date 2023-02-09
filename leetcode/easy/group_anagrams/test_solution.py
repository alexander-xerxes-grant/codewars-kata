import pytest

from .solution import Solution


class TestSolution:
    
    @pytest.fixture
    def solution(self) -> Solution:
        return Solution()
    
    def test_group_anagrams(self, solution):
        
        assert solution.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat","tea","ate"], ["tan","nat"], ["bat"]]
        assert solution.group_anagrams([""]) == [[""]]
        assert solution.group_anagrams(["a"]) == [["a"]]