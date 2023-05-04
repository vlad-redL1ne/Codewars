import importlib
from asserts.asserts import assert_true

title_case = importlib.import_module('katas.6kyu.Title Case.solution').title_case


class TestSolution:
    def test_title_case(self):
        assert_true(title_case(''), '')
        assert_true(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
        assert_true(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
        assert_true(title_case('the quick brown fox'), 'The Quick Brown Fox')
        assert_true(title_case('a bc', 'bc'), 'A bc')
