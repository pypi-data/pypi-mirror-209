from typing import Optional


def multi(f):
    return isinstance(
        f, (list, set, frozenset, tuple, type({}.values()), type({}.keys()))
    )


def pop(data, key, default=None):
    if isinstance(data, dict):
        return data.pop(key) if key in data else default
    elif isinstance(data, list):
        return data.pop(key) if key < len(data) else default
    return default


def copy_value(data):
    """
    return a new value identical to default , but different in memory,
    to avoid multiple initialize to modify the same default data
    """
    if multi(data):
        return type(data)([copy_value(d) for d in data])
    elif isinstance(data, dict):
        return {k: copy_value(v) for k, v in data.items()}
    return data


def get_name(func) -> Optional[str]:
    if isinstance(func, str):
        return func
    if isinstance(func, property):
        func = func.fget
    from functools import partial

    if isinstance(func, partial):
        if hasattr(func, "__name__"):
            return func.__name__
        func = func.func
    if hasattr(func, "__name__"):
        return func.__name__
    return None
