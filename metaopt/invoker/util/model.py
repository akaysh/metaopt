"""
Models for data exchange between processes.
"""
from __future__ import division, print_function, with_statement

from collections import namedtuple

# data structure for errors generated by the workers
Error = namedtuple("Error", ["worker_id", "task", "value"])

# data structure for results generated by the workers
Result = namedtuple("Result", ["worker_id", "task", "value"])

# data structure for workers leaving the work force
Release = namedtuple("Release", ["worker_id", "task"])

# data structure for declaring the start of an execution by the workers
Start = namedtuple("Start", ["worker_id", "task"])

# data structure for tasks given to the workers
Task = namedtuple("Task", ["id", "function", "args", "kwargs"])
