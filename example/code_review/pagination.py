"""A standalone pagination example for code review."""


def paginate(items, page=1, page_size=10):
    """Return a new list for a one-based page of a sliceable sequence.

    Empty input and pages beyond the end return an empty list. Page and
    page_size must be positive integers; booleans are not valid page numbers.
    """
    for name, value in (("page", page), ("page_size", page_size)):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be positive".format(name))

    start = (page - 1) * page_size
    return list(items[start:start + page_size])
