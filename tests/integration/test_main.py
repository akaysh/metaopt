"""
Integration test for main.py.
"""

from __future__ import division, print_function, with_statement

from tests.util.integer_functions import g as f

from nose.tools import eq_

from orges.core.main import optimize
from orges.optimizer.gridsearch import GridSearchOptimizer


def test_optimize_running_too_long_aborts():
    optimizer = GridSearchOptimizer()
    result = optimize(f, timeout=1, optimizer=optimizer)

    # f(a=0) is 0, f(a=1) is -1. Because of the timeout we never see a=1, hence
    # we except the minimum before the timeout to be 0.
    eq_(result[0].value, 0)


if __name__ == '__main__':
    import nose
    nose.runmodule()