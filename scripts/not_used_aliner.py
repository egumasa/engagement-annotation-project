import itertools


def align_iterables(inputs, missing=None):
    """Align sorted iterables

    Yields tuples with values from the respective `inputs`, placing
    `missing` if the value does not exist in the corresponding
    iterable.

    Example: align_generator('bc', 'bf', '', 'abf') yields:
        (None, None, None, 'a')
        ('b', 'b', None, 'b')
        ('c', None, None, None)
        (None, 'f', None, 'f')
    """
    End = object()
    iterators = [itertools.chain(i, [End]) for i in inputs]
    values = [next(i) for i in iterators]
    while not all(v is End for v in values):
        smallest = min(v for v in values if v is not End)
        yield tuple(v if v == smallest else missing for v in values)
        values = [next(i) if v == smallest else v
                  for i, v in zip(iterators, values)]

def align_two_lists(list1, list2, missing="MISSING"):
    value = list(zip(*list(align_iterables([list1, list2], missing=missing))))
    if not value:
        return [[], []]
    else:
        a, b = value
        return [list(a), list(b)]
