import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.4kyu.Counting Change Combinations.solution').count_change

cases = [
    TestCase()
]


class TestSolution:

    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_counting_change_combinations(self, test):
        assert_true(solution(test.test_data), test.test_output)
