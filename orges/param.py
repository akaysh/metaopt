# -*- coding: utf-8 -*-
"""

This module provides decorators to specify the parameters of a function without
using an explicit param_spec object. For example::

    import orges.param as param

    @param.int("a", interval=(1, 10), step=2, display_name="α")
    @param.float("b", interval=(0, 1), display_name"β")
    @param.bool("g", display_name="γ")
    def some_function(a, b, c):
        pass

This code specifies that some_function takes 3 parameters ``a``, ``b``, and
``g`` each with their own interval, step size and display name.

"""

from __future__ import division, print_function, with_statement

from orges.paramspec import ParamSpec


def int(*vargs, **kwargs):
    """A decorator that specifies an int parameter for a function"""

    def decorator(func):
        param_spec = make_param_spec(func)
        param_spec.int(*vargs, **kwargs)
        return func

    return decorator


def float(*vargs, **kwargs):
    """A decorator that specifies a float parameter for a function"""

    def decorator(func):
        param_spec = make_param_spec(func)
        param_spec.float(*vargs, **kwargs)
        return func

    return decorator


def bool(*vargs, **kwargs):
    """A decorator that specifies an bool parameter for a function"""
    def decorator(func):
        param_spec = make_param_spec(func)
        param_spec.bool(*vargs, **kwargs)
        return func

    return decorator


def make_param_spec(func):
    """Create a new param_spec object for ``f`` or retrieves it if it exists"""
    try:
        param_spec = func.param_spec
    except AttributeError:
        func.param_spec = param_spec = ParamSpec(via_decorator=True)
    return param_spec
