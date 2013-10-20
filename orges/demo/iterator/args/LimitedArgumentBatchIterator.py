"""
Iterator that wraps around a task iterator, limiting it's results.
"""


class LimitedArgumentBatchIterator(object):
    """Iterator that wraps around a task iterator, limiting it's results."""
    def __init__(self, argument_batch_iterator, limit):
        self.task_iterator = argument_batch_iterator
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def next(self):
        if self.count == self.limit:
            raise StopIteration
        self.count += 1
        return next(self.task_iterator)
