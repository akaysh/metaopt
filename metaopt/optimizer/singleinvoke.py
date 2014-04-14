# -*- coding: utf-8 -*-
"""
Optimizer that issues one single invocation, only.
"""
from __future__ import division, print_function, with_statement

from metaopt.core.args import ArgsCreator
from metaopt.optimizer.base import BaseCaller, BaseOptimizer
from metaopt.util.stoppable import StoppedException


class SingleInvokeOptimizer(BaseOptimizer, BaseCaller):
    """
    Optimizer that issues one single invocation, only.
    """
    def __init__(self):
        super(SingleInvokeOptimizer, self).__init__()
        self._result = None

    def optimize(self, invoker, function, param_spec, return_spec):
        del function  # TODO implement me
        del return_spec  # TODO implement me
        args = ArgsCreator(param_spec).args()

        try:
            invoker.invoke(self, args)
        except StoppedException:
            return None

        invoker.wait()
        return self._result

    def on_error(self, error, fargs, **kwargs):
        # TODO implement me
        pass

    def on_result(self, result, fargs, **kwargs):
        del fargs
        del kwargs
        self._result = result
