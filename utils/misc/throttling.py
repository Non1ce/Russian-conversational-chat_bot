# -*- coding: utf-8 -*-

"""


Created on 10.09.2021

@author: Nikita


"""


def rate_limit(limit: int, key=None):

    """

    Decorator for configuring rate limit and key in different functions.

    """

    def decorator(func):

        setattr(func, 'throttling_rate_limit', limit)

        if key:
            setattr(func, 'throttling_key', key)

        return func

    return decorator
