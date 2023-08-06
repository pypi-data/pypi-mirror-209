import copy
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

from katalytic.data.checks import (
    is_any_of, is_generator, is_iterable, is_iterator, is_none_of, is_primitive, is_dict_of_sequences_uniform, is_sequence_of_sequences_uniform,
    is_sequence_of_dicts_uniform
)

from katalytic.pkg import get_version

__version__, __version_info__ = get_version(__name__)
_UNDEFINED = object()


def _function(): pass
def _generator(): yield 1


class _C:
    def __call__(self, *args, **kwargs):
        pass


_map = map(int, [])
_C_obj = _C()
_obj = object()
_lambda = lambda x: x
_generator_expr = (x for x in [])
_sequences = [[], (), range(0)]
_dict_views = [{}.keys(), {}.values(), {}.items()]
_iterators = [_generator, _generator_expr, iter([]), _map, enumerate([]), zip([], [])]
_iterables = [*_dict_views, *_iterators, *_sequences, set(), {}]
_collections = [(), set(), frozenset([]), {}, []]
_booleans = [True, False]
_singletons = [None, True, False]
_primitives = [*_singletons, 0, 0.0, '', b'', bytearray(b'')]
_callables = [_generator, _function, _lambda, _C_obj, _C]
_numbers = [0, 0.0, 0j, Decimal('0'), Fraction(0, 1)]
_objects = [_obj, _C_obj]
_generators = [_generator, _generator_expr]
_functions = [_generator, _function, _lambda]
_strings = ['', b'', bytearray(b'')]

_types = {
    'booleans': _booleans,
    'bytearray': bytearray(b''),
    'bytes': b'',
    'callables': _callables,
    'callable_obj': _C_obj,
    'class': _C,
    'collections': _collections,
    'complex': 0 + 0j,
    'decimal': Decimal('0'),
    'dict': {},
    'dict_views': _dict_views,
    'float': 0.0,
    'fraction': Fraction(0, 1),
    'frozenset': frozenset([]),
    'functions': _functions,
    'generator_expression': _generator_expr,
    'generator_function': _generator,
    'generators': _generators,
    'int': 0,
    'iterables': _iterables,
    'iterators': _iterators,
    'list': [],
    'map': _map,
    'none': None,
    'numbers': _numbers,
    'objects': _objects,
    'path': Path(''),
    'primitives': _primitives,
    'sequences': _sequences,
    'set': set(),
    'singletons': _singletons,
    'str': '',
    'strings': _strings,
    'tuple': (),
}


def all_types(whitelist=None):
    if whitelist is None:
        return _flatten(_types.values())
    elif isinstance(whitelist, str):
        whitelist = [whitelist]
    elif not is_iterable(whitelist):
        raise TypeError(f'<whitelist> must be iterable. Got {type(whitelist).__name__}')

    unexpected = set(whitelist) - set(_types.keys())
    if unexpected:
        raise ValueError(f'Unexpected types in <whitelist>: {unexpected}')

    return _flatten(_types[t] for t in whitelist)


def all_types_besides(blacklist):
    if isinstance(blacklist, str):
        blacklist = [blacklist]
    elif not is_iterable(blacklist):
        raise TypeError(f'<blacklist> must be iterable. Got {type(blacklist).__name__}')

    blacklist = set(blacklist)
    unexpected = blacklist - set(_types.keys())
    if unexpected:
        raise ValueError(f'Unexpected types in <blacklist>: {unexpected}')

    to_remove = _flatten(_types[t] for t in blacklist)
    all_types = _flatten(_types.values())
    kept = []
    for t in all_types:
        if t in to_remove:
            continue

        # remove duplicates too
        # I have to do it this way because python considers
        # 0 == 0.0 == 0j == Decimal('0') == Fraction(0, 1)
        if (t, type(t)) in [(x, type(x)) for x in kept]:
            continue

        kept.append(t)

    return kept


def _flatten(iterable):
    if not is_iterable(iterable):
        raise TypeError(f'<iterable> expects an iterable. Got {type(iterable).__name__}')

    flat = []
    for x in iterable:
        if isinstance(x, (dict, set, list, tuple)) and len(x):
            flat.extend(x)
        else:
            flat.append(x)

    return flat


def as_dict_of_lists(data):
    """This format is useful when you need to perform operations on each column
    of a table.

    It's as compact as the sequence_of_sequences format, but less intuitive"""
    if is_sequence_of_dicts_uniform(data):
        return {k: [d[k] for d in data] for k in data[0]}
    elif is_sequence_of_sequences_uniform(data):
        return {k: [v[i] for v in data[1:]] for i, k in enumerate(data[0])}
    elif is_dict_of_sequences_uniform(data):
        return {k: list(v) for k, v in data.items()}
    else:
        raise TypeError(f'Unexpected format for <data>. Got {type(data).__name__}: {data!r}')


def as_list_of_dicts(data):
    """This format is useful when you need to perform operations on each row of a table"""
    if is_sequence_of_dicts_uniform(data):
        header = list(data[0].keys())
        return [{k: d[k] for k in header} for d in data]
    elif is_sequence_of_sequences_uniform(data):
        return [dict(zip(data[0], row)) for row in data[1:]]
    elif is_dict_of_sequences_uniform(data):
        first_seq = list(data.values())[0]
        seq_len = len(first_seq)
        return [{k: v[i] for k, v in data.items()} for i in range(seq_len)]
    else:
        raise TypeError(f'Unexpected format for <data>. Got {type(data).__name__}: {data!r}')


def as_list_of_lists(data):
    """This and the dict_of_sequences formats are the most compact for storing
    tabular data. This one is more intuitive than the dict_of_sequences format"""
    if is_sequence_of_dicts_uniform(data):
        header = [list(data[0].keys())]
        rows = [[d[k] for k in header[0]] for d in data]
        return header + rows
    elif is_sequence_of_sequences_uniform(data):
        return list(map(list, data))
    elif is_dict_of_sequences_uniform(data):
        header = [list(data.keys())]
        n = len(list(data.values())[0])
        rows = [[v[i] for v in data.values()] for i in range(n)]
        return header + rows
    else:
        raise TypeError(f'Unexpected format for <data>. Got {type(data).__name__}: {data!r}')


def detect_fronts(bits):
    """Detects the fronts in a sequence of bits.
    A front is a change from 0 to 1 (positive) or from 1 to 0 (negative)
    It works even if the bits are booleans instead of 0/1

    Returns a list of tuples (index, change) where index is the index
    at which the bit flip takes place and change is 1 for positive fronts
    and -1 for negative fronts.
    """
    if is_iterator(bits):
        bits = list(bits)
    elif isinstance(bits, str):
        bits = list(map(int, bits))

    if not all(is_any_of(b, (0, 1, True, False)) for b in bits):
        raise TypeError(f'Only 0/1 or True/False are allowed. Got {bits!r}')

    fronts = []
    for i, (a, b) in enumerate(zip(bits, bits[1:])):
        if (a, b) == (0, 1):
            fronts.append((i+1, 1))
        elif (a, b) == (1, 0):
            fronts.append((i+1, -1))

    return fronts


def detect_fronts_positive(bits):
    """Detects the positive fronts (a 0 to 1 transition).
    It works even if the bits are booleans instead of 0/1
    Returns a list of indices at which the bit flip takes place.
    """
    return [i for i, change in detect_fronts(bits) if change == 1]


def detect_fronts_negative(bits):
    """Detects the negative fronts (a 1 to 0 transition).
    It works even if the bits are booleans instead of 0/1
    Returns a list of indices at which the bit flip takes place.
    """
    return [i for i, change in detect_fronts(bits) if change == -1]


def first(data, *, key=lambda _: True):
    if isinstance(data, set):
        raise TypeError(f'<data> expects a sequence. Got set. Use `one(data)` instead')

    return one(data, key=key)


def first_with_idx(data, *, key=lambda _: True):
    """When no item is found, returns None instead of (None, None).
    (None, None) lets you use unpacking everywhere, but it's a bad idea because
    it's evaluated as truthy in `if first_with_idx(...): ...`
    It would lead to a lot of counter-intuitive bugs, so it's better to avoid it
    """
    if isinstance(data, set):
        raise TypeError(f'<data> expects a sequence. Got set. Use `one(data)` instead')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    for i, v in enumerate(data):
        if key(v):
            return (i, v)

    return None


def flatten(iterable):
    if not is_iterable(iterable):
        raise TypeError(f'<iterable> expects an iterable. Got {type(iterable).__name__}')

    flat = []
    for x in iterable:
        if is_iterable(x):
            flat.extend(x)
        else:
            flat.append(x)

    return flat


def flatten_recursive(iterable):
    new = flatten(iterable)
    if new == iterable:
        return new
    else:
        return flatten_recursive(new)


def last(data, *, key=lambda _: True):
    if isinstance(data, set):
        raise TypeError(f'<data> expects a sequence. Got set. Use `one(data)` instead')

    if is_iterator(data) or isinstance(data, dict):
        data = list(data)

    return one(reversed(data), key=key)


def last_with_idx(data, *, key=lambda _: True):
    """When no item is found, returns None instead of (None, None).
    (None, None) lets you use unpacking everywhere, but it's a bad idea because
    it's evaluated as truthy in `if first_with_idx(...): ...`
    It would lead to a lot of counter-intuitive bugs, so it's better to avoid it
    """
    if isinstance(data, set):
        raise TypeError(f'<data> expects a sequence. Got set. Use `one(data)` instead')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    if is_iterator(data) or isinstance(data, dict):
        data = list(data)

    for i, v in enumerate(reversed(data), start=1):
        if key(v):
            return (len(data) - i, v)

    return None


def map_dict_keys(f, data, *, condition=None):
    if not callable(f):
        raise TypeError(f'<f> expects a function. Got {type(f).__name__}: {f!r}')
    elif not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not(condition is None or callable(condition)):
        raise TypeError(f'<condition> expects None or a function. Got {type(condition).__name__}: {condition!r}')

    if condition is None:
        return {f(k): v for k, v in data.items()}
    else:
        return {f(k) if condition(k) else k: v for k, v in data.items()}


def map_dict_values(f, data, *, condition=None):
    if not callable(f):
        raise TypeError(f'<f> expects a function. Got {type(f).__name__}: {f!r}')
    elif not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not(condition is None or callable(condition)):
        raise TypeError(f'<condition> expects None or a function. Got {type(condition).__name__}: {condition!r}')

    if condition is None:
        return {k: f(v) for k, v in data.items()}
    else:
        return {k: f(v) if condition(v) else v for k, v in data.items()}


def map_recursive(f, data, *, condition=is_primitive, on_dict_keys=False):
    if not callable(f):
        raise TypeError(f'<f> expects a function. Got {type(f).__name__}: {f!r}')
    elif not is_iterable(data):
        raise TypeError(f'<data> expects an iterable. Got {type(data).__name__}: {data!r}')
    elif not(condition is None or callable(condition)):
        raise TypeError(f'<condition> expects None or a function. Got {type(condition).__name__}: {condition!r}')
    elif not isinstance(on_dict_keys, bool):
        raise TypeError(f'<on_dict_keys> expects True or False. Got {type(on_dict_keys).__name__}: {on_dict_keys!r}')

    if is_iterator(data):
        new_data = (
            map_recursive(f, v, condition=condition, on_dict_keys=on_dict_keys)
            if is_iterable(v) else f(v) if condition(v) else v for v in data
        )
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            if on_dict_keys:
                if is_iterable(k):
                    k = map_recursive(f, k, condition=condition, on_dict_keys=on_dict_keys)
                if condition(k):
                    k = f(k)

            if is_iterable(v):
                v = map_recursive(f, v, condition=condition, on_dict_keys=on_dict_keys)
            if condition(v):
                v = f(v)

            new_data[k] = v
    else:
        new_data = type(data)(
            map_recursive(f, v, condition=condition, on_dict_keys=on_dict_keys)
            if is_iterable(v) else f(v) if condition(v) else v for v in data
        )

    if condition(new_data):
        return f(new_data)
    else:
        return new_data


def one(data, *, key=lambda _: True):
    if not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')
    elif not is_iterable(data):
        raise TypeError(f'<data> expects an iterable. Got {type(data).__name__}: {data!r}')

    try:
        return next(filter(key, data))
    except StopIteration:
        return None


def pop_min(data, *, key=lambda x: x, default=_UNDEFINED):
    """Removes and returns the minimum element from the collection.
    If key is specified, the minimum element is determined by the key.
    """
    if not is_iterable(data):
        raise TypeError(f'<data> expects an iterable. Got {type(data).__name__}: {data!r}')
    elif isinstance(data, dict):
        raise TypeError(f'<data> expects any iterable besides dict. For dict, use `pop_min_key` or `pop_min_value` instead')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    original_type = type(data)
    data = [copy.deepcopy(item) for item in data]
    found = min(data, key=key, default=_UNDEFINED)
    if found is _UNDEFINED and default is _UNDEFINED:
        raise ValueError('Cannot pop from an empty collection unless a default value is provided')

    data.remove(found)
    if original_type in (list, tuple, set, frozenset):
        return found, original_type(data)
    else:
        return found, data


def pop_max(data, *, key=lambda x: x, default=_UNDEFINED):
    """Removes and returns the maximum element from the collection.
    If key is specified, the maximum element is determined by the key.
    """
    if not is_iterable(data):
        raise TypeError(f'<data> expects an iterable. Got {type(data).__name__}: {data!r}')
    elif isinstance(data, dict):
        raise TypeError(f'<data> expects any iterable besides dict. For dict, use `pop_max_key` or `pop_max_value` instead')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    original_type = type(data)
    data = [copy.deepcopy(item) for item in data]
    found = max(data, key=key, default=_UNDEFINED)
    if found is _UNDEFINED and default is _UNDEFINED:
        raise ValueError('Cannot pop from an empty collection unless a default value is provided')

    data.remove(found)
    if original_type in (list, tuple, set, frozenset):
        return found, original_type(data)
    else:
        return found, data


def pop_max_by_dict_key(data, *, key=lambda x: x, default=_UNDEFINED):
    """Removes and returns the maximum (kay, value) pair from the dict based on the dict key.

    If the <key> arg is specified, it will be used to calculate the maximum.
    This key is the function by which to calculate the max, not the dict key
    """
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    data = copy.deepcopy(data)
    dict_key = max(data.keys(), key=key, default=_UNDEFINED)
    if dict_key is _UNDEFINED and default is _UNDEFINED:
        raise ValueError('Cannot pop from an empty dict unless a default value is provided')

    value = data.pop(dict_key)
    return (dict_key, value), data


def pop_min_by_dict_key(data, *, key=lambda x: x, default=_UNDEFINED):
    """Removes and returns the minimum (kay, value) pair from the dict based on the dict key.

    If the <key> arg is specified, it will be used to calculate the minimum.
    This key is the function by which to calculate the min, not the dict key
    """
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    data = copy.deepcopy(data)
    dict_key = min(data.keys(), key=key, default=_UNDEFINED)
    if dict_key is _UNDEFINED and default is _UNDEFINED:
        raise ValueError('Cannot pop from an empty dict unless a default value is provided')

    value = data.pop(dict_key)
    return (dict_key, value), data


def pop_max_by_dict_value(data, *, key=lambda x: x, default=_UNDEFINED):
    """Removes and returns the maximum (kay, value) pair from the dict based on the dict key.

    If the <key> arg is specified, it will be used to calculate the maximum.
    This key is the function by which to calculate the max, not the dict key
    """
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    data = copy.deepcopy(data)
    item = max(data.items(), key=lambda kv: key(kv[1]), default=_UNDEFINED)
    if item is _UNDEFINED and default is _UNDEFINED:
        raise ValueError('Cannot pop from an empty dict unless a default value is provided')

    _ = data.pop(item[0])
    return item, data


def pop_min_by_dict_value(data, *, key=lambda x: x, default=_UNDEFINED):
    """Removes and returns the minimum (kay, value) pair from the dict based on the dict key.

    If the <key> arg is specified, it will be used to calculate the minimum.
    This key is the function by which to calculate the min, not the dict key
    """
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}: {key!r}')

    data = copy.deepcopy(data)
    item = min(data.items(), key=lambda kv: key(kv[1]), default=_UNDEFINED)
    if item is _UNDEFINED and default is _UNDEFINED:
        raise ValueError('Cannot pop from an empty dict unless a default value is provided')

    _ = data.pop(item[0])
    return item, data


def pick_all(needles, haystack):
    if not is_iterable(needles):
        raise TypeError(f'<needles> expects an iterable. Got {type(needles).__name__}: {needles!r}')
    elif not is_iterable(haystack):
        raise TypeError(f'<haystack> expects an iterable. Got {type(haystack).__name__}: {haystack!r}')

    return [needle for needle in needles if is_any_of(needle, haystack)]


def pick_all_besides(needles, haystack):
    if not is_iterable(needles):
        raise TypeError(f'<needles> expects an iterable. Got {type(needles).__name__}: {needles!r}')
    elif not is_iterable(haystack):
        raise TypeError(f'<haystack> expects an iterable. Got {type(haystack).__name__}: {haystack!r}')

    return [needle for needle in needles if is_none_of(needle, haystack)]


def pick_any(needles, haystack):
    if not is_iterable(needles):
        raise TypeError(f'<needles> expects an iterable. Got {type(needles).__name__}: {needles!r}')
    elif not is_iterable(haystack):
        raise TypeError(f'<haystack> expects an iterable. Got {type(haystack).__name__}: {haystack!r}')

    for needle in needles:
        if is_any_of(needle, haystack):
            return needle

    return None


def sort_dict_by_keys(data, *, key=None, reverse=False):
    """key is the "metric" to sort by, not the dict's key"""
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not(key is None or callable(key)):
        raise TypeError(f'<key> expects None or a function. Got {type(key).__name__}: {key!r}')
    elif not isinstance(reverse, bool):
        raise TypeError(f'<reverse> expects True or False. Got {type(reverse).__name__}: {reverse!r}')

    if key is None:
        return dict(sorted(data.items(), reverse=reverse))
    else:
        return dict(sorted(data.items(), key=lambda kv: key(kv[0]), reverse=reverse))


def sort_dict_by_keys_recursive(data, *, key=None, reverse=False):
    """key is the "metric" to sort by, not the dict's key"""
    if not is_iterable(data):
        raise TypeError(f'<data> expects an iterable. Got {type(data).__name__}: {data!r}')
    elif not(key is None or callable(key)):
        raise TypeError(f'<key> expects None or a function. Got {type(key).__name__}: {key!r}')
    elif not isinstance(reverse, bool):
        raise TypeError(f'<reverse> expects True or False. Got {type(reverse).__name__}: {reverse!r}')

    if isinstance(data, dict):
        return sort_dict_by_keys({k: sort_dict_by_keys_recursive(v, key=key, reverse=reverse) if is_iterable(v) else v for k, v in data.items()}, key=key, reverse=reverse)
    elif is_iterator(data):
        return (sort_dict_by_keys_recursive(v, key=key, reverse=reverse) if is_iterable(v) else v for v in data)
    elif is_iterable(data):
        return type(data)(sort_dict_by_keys_recursive(v, key=key, reverse=reverse) if is_iterable(v) else v for v in data)


def sort_dict_by_values(data, *, key=None, reverse=False):
    """key is the "metric" to sort by, not the dict's key"""
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}: {data!r}')
    elif not(key is None or callable(key)):
        raise TypeError(f'<key> expects None or a function. Got {type(key).__name__}: {key!r}')
    elif not isinstance(reverse, bool):
        raise TypeError(f'<reverse> expects True or False. Got {type(reverse).__name__}: {reverse!r}')

    if key is None:
        return dict(sorted(data.items(), key=lambda kv: kv[1], reverse=reverse))
    else:
        return dict(sorted(data.items(), key=lambda kv: key(kv[1]), reverse=reverse))


def sort_dict_by_values_recursive(data, *, key=None, reverse=False):
    """key is the "metric" to sort by, not the dict's key"""
    if not is_iterable(data):
        raise TypeError(f'<data> expects an iterable. Got {type(data).__name__}: {data!r}')
    elif not(key is None or callable(key)):
        raise TypeError(f'<key> expects None or a function. Got {type(key).__name__}: {key!r}')
    elif not isinstance(reverse, bool):
        raise TypeError(f'<reverse> expects True or False. Got {type(reverse).__name__}: {reverse!r}')

    if isinstance(data, dict):
        return sort_dict_by_values({k: sort_dict_by_values_recursive(v, key=key, reverse=reverse) if is_iterable(v) else v for k, v in data.items()}, key=key, reverse=reverse)
    elif is_iterator(data):
        return (sort_dict_by_values_recursive(v, key=key, reverse=reverse) if is_iterable(v) else v for v in data)
    elif is_iterable(data):
        return type(data)(sort_dict_by_values_recursive(v, key=key, reverse=reverse) if is_iterable(v) else v for v in data)


def sort_recursive(data, *, key=lambda x: x, reverse=False, sort_dicts_by='keys', sort_iters=True, sort_lists=True, sort_sets=True, sort_tuples=True):
    """Sort the inner collection first, then the outer one"""
    if not is_iterable(data):
        raise TypeError(f'<data> expects an iterable. Got {type(data).__name__}')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}')
    elif not isinstance(reverse, bool):
        raise TypeError(f'<reverse> expects True or False. Got {type(reverse).__name__}')
    elif is_none_of(sort_dicts_by, ('keys', 'values', None)):
        raise ValueError(f'<sort_dicts_by> expects "keys", "values" or None. Got {sort_dicts_by!r}')
    elif not isinstance(sort_iters, bool):
        raise TypeError(f'<sort_iters> expects True or False. Got {type(sort_iters).__name__}')
    elif not isinstance(sort_lists, bool):
        raise TypeError(f'<sort_lists> expects True or False. Got {type(sort_lists).__name__}')
    elif not isinstance(sort_sets, bool):
        raise TypeError(f'<sort_sets> expects True or False. Got {type(sort_sets).__name__}')
    elif not isinstance(sort_tuples, bool):
        raise TypeError(f'<sort_tuples> expects True or False. Got {type(sort_tuples).__name__}')

    initial_type = type(data)
    kwargs = {
        'key': key,
        'reverse': reverse,
        'sort_dicts_by': sort_dicts_by,
        'sort_iters': sort_iters,
        'sort_lists': sort_lists,
        'sort_sets': sort_sets,
        'sort_tuples': sort_tuples,
    }

    if isinstance(data, dict):
        # You shouldn't sort the keys, even if they are tuple,
        # as they are likely to be used as IDs
        inner_sorted = {k: sort_recursive(v, **kwargs) if is_iterable(v) else v for k, v in data.items()}
        if sort_dicts_by == 'keys':
            return sort_dict_by_keys(inner_sorted, key=key, reverse=reverse)
        elif sort_dicts_by == 'values':
            return sort_dict_by_values(inner_sorted, key=key, reverse=reverse)
        else:
            return inner_sorted

    inner_sorted = (sort_recursive(v, **kwargs) if is_iterable(v) else v for v in data)
    if is_iterator(data) and not sort_iters:
        return inner_sorted
    elif isinstance(data, list) and not sort_lists:
        return list(inner_sorted)
    elif isinstance(data, set) and not sort_sets:
        return set(inner_sorted)
    elif isinstance(data, tuple) and not sort_tuples:
        return tuple(inner_sorted)
    elif is_iterator(data) or isinstance(data, (set, list, tuple)):
        data = sorted(inner_sorted, key=key, reverse=reverse)
        if initial_type == tuple:
            return tuple(data)
        else:
            return data
    else:  # pragma: no cover
        raise AssertionError(f'Unexpected branch for <data> of type {type(data).__name__}')


def swap_keys_and_values(data):
    if not isinstance(data, dict):
        raise TypeError(f'<data> expects a dict. Got {type(data).__name__}')

    return {v: k for k, v in data.items()}


def xor(*values, key=bool):
    if len(values) < 2:
        raise ValueError('<values> expects at least two values')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}')

    v = None
    for value in values:
        if key(value):
            if v is None:
                v = value
            else:
                return None

    return v


def xor_with_idx(*values, key=bool):
    if len(values) < 2:
        raise ValueError('<values> expects at least two values')
    elif not callable(key):
        raise TypeError(f'<key> expects a function. Got {type(key).__name__}')

    v = None
    for i, value in enumerate(values):
        if key(value):
            if v is None:
                v = (i, value)
            else:
                return None

    return v
