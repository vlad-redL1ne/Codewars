import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Make the Deadfish swim.solution').parse

cases = [
    Case("ooo", [0, 0, 0]),
    Case("ioioio", [1, 2, 3]),
    Case('isoisoiso', [1, 4, 25]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_make_the_deadfish_swim(self, test):
        assert_true(solution(test.test_data), test.test_output)
