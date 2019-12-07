import pytest
from functools import wraps
class TestDecorators:
    def logit(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            print(func.__name__ + " was called")
            return func(*args, **kwargs)
        return with_logging

    @logit
    def addition_func(x):
        return x + x