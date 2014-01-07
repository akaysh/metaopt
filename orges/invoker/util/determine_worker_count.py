"""
Utility to determine the number of workers that can run.
"""
from __future__ import division, print_function, with_statement

from multiprocessing import cpu_count


def determine_worker_count(request=None):
    """
    Determines the maximum number of worker processes or threads.

    If there are more physical or virtual CPUs available on this machine than
    the number of requested request, that is returned.
    """
    if request is None:
        try:
            # attempt automatic configuration
            return cpu_count()
        except NotImplementedError:
            # assume single core, to be safe
            return 1
    if type(request) is not int:
        raise NotImplementedError("Request parameter needs to be of type int.")
    if request <= 0:
        raise NotImplementedError("Request parameter needs to be greater 0.")
    return request