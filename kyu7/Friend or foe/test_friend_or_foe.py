import importlib

from asserts.Asserts import assert_true

friend = importlib.import_module('kyu7.Friend or foe.solution').friend


class TestSolution:
    def test_friend_or_foe(self):
        assert_true(friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])
