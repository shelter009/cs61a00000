def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    ret = 0
    if m == 1 and n == 1:
        return 1
    if m > 1:
        ret += paths(m-1,n)
    if n > 1:
        ret += paths(m,n-1)
    return ret

print(paths(2,2))