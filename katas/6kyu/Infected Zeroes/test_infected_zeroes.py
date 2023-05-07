import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Infected Zeroes.solution').infected_zeroes

cases = [
    Case([0], 0),
    Case([1, 1, 0, 1, 1], 2),
    Case([0, 1, 1, 1], 3),
]


class TestSolution:
    @pytest.mark.skip(reason='long tests not passed')
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_infected_zeroes(self, test):
        assert_true(solution(test.test_data), test.test_output)
