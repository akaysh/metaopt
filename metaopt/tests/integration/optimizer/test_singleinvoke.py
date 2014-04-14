"""
TODO document me
"""
from __future__ import division, print_function, with_statement

from mock import Mock

from metaopt.core import param
from metaopt.core.args import ArgsCreator
from metaopt.core.returnspec import ReturnValuesWrapper
from metaopt.invoker.singleprocess import SingleProcessInvoker
from metaopt.optimizer.singleinvoke import SingleInvokeOptimizer


@param.int("a", interval=(2, 2))
@param.int("b", interval=(1, 1))
def f(a, b):
    return -(a + b)


def test_optimize_returns_result():
    optimizer = SingleInvokeOptimizer()
    optimizer.on_result = Mock()
    optimizer.on_error = Mock()

    invoker = SingleProcessInvoker()
    invoker.f = f

    optimizer.optimize(invoker=invoker, function=f,
                       param_spec=f.param_spec, return_spec=None)

    args = ArgsCreator(f.param_spec).args()

    assert not optimizer.on_error.called
    optimizer.on_result.assert_called_with(ReturnValuesWrapper(None, -3), args)

if __name__ == '__main__':
    import nose
    nose.runmodule()
