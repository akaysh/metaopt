"""
Tests for the main module.
"""

from __future__ import division, print_function, with_statement

from nose.tools import raises

from orges.core.main import custom_optimize, NoParamSpecError
from orges.invoker.simple import SimpleInvoker


def f(x, y):
    pass


@raises(NoParamSpecError)
def test_custom_optimize_given_no_param_spec_complains():
    custom_optimize(f, SimpleInvoker())

if __name__ == '__main__':
    import nose
    nose.runmodule()
