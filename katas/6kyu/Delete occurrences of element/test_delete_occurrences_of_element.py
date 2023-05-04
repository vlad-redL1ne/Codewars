import importlib
from asserts.asserts import assert_true

delete_nth = importlib.import_module('katas.6kyu.Delete occurrences of element.solution').delete_nth


class TestSolution:
    def test_delete_occurrences_of_element(self):
        assert_true(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
        assert_true(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
