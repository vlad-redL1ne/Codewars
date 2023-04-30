import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Smash kata.solution').smash

cases = [
    TestCase(['hello', 'world'], 'hello world'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_permutations(self, test):
        assert_true(solution(test.test_data), test.test_output)
