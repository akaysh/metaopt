# -*- coding: utf-8 -*-
"""
Tests for the main module.
"""

# Future
from __future__ import absolute_import, division, print_function, \
    unicode_literals, with_statement

# Third Party
import nose
from mock import Mock
from nose.tools import raises

# First Party
from metaopt.core.main import NoParamSpecError, custom_optimize
from metaopt.invoker.dualthread import DualThreadInvoker


def f(x, y):
    pass


def test_custom_optimize_stops_invoker():
    invoker = Mock()
    invoker.stop = Mock()

    optimizer = Mock()
    optimizer.optimize = Mock()
    optimizer.optimize.return_value = (1, 0)

    param_spec = Mock()
    return_spec = Mock()

    custom_optimize(f, invoker, optimizer=optimizer, param_spec=param_spec,
        return_spec=return_spec)

    assert invoker.stop.called


@raises(NoParamSpecError)
def test_custom_optimize_given_no_param_spec_complains():
    custom_optimize(f, DualThreadInvoker())

if __name__ == '__main__':
    nose.runmodule()