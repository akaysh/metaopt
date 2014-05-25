# -*- coding: utf-8 -*-
"""
SVM (SAES, global timeout)
================================
"""
# Future
from __future__ import absolute_import, division, print_function, \
    unicode_literals, with_statement

# Standard Library
from time import sleep

# Third Party
import nose

# First Party
from metaopt.core.optimize.optimize import optimize
from metaopt.core.paramspec.util import param
from metaopt.core.returnspec.util.decorator import maximize
from metaopt.optimizer.gridsearch import GridSearchOptimizer
from metaopt.plugin.timeout import TimeoutPlugin


@maximize("Score")
@param.float("a", interval=[0.1, 0.5], step=0.05)
def f(a):
    sleep(a)
    return a


class TestTimings(object):

    def test_all_timings(self):
        for timeout_local in [0.05 * i for i in range(5)]:
            for timeout_global in [0.05 * o for o in range(5)]:
                optimizer = GridSearchOptimizer()
                plugins = [TimeoutPlugin(timeout_local)]

                optimize(f=f, timeout=timeout_global, optimizer=optimizer,
                                   plugins=plugins)


if __name__ == '__main__':
    nose.runmodule()
