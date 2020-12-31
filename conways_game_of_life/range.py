"""
range.py.

A simplified version of Python's range type.
"""

from math import ceil


class Range:
    """Represents a fixed sequence of integers.

    The sequence is defined by an inclusive start, an exclusive end,
    and a step value between adjacent integers in the sequence.
    """

    def __init__(self, start, stop, step=1):
        """Construct this range with the given start, stop, and step.

        Requires start, stop, and step to be integers, and step to be
        positive.
        """
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Return an iterator object over this sequence."""
        return RangeIter(self.start, self.stop, self.step)

    def __len__(self):
        """Return the length of this sequence."""
        # add your code below

    def __contains__(self, i):
        """Return whether the given integer is in this range."""
        # add your code below


class RangeIter:
    """An iterator over a range of integers."""

    def __init__(self, start, stop, step):
        """Construct an iterator with the given start, stop, and step.

        Requires start, stop, and step to be integers, and step to be
        positive.
        """
        # add your code below

    def __iter__(self):
        """Return this object."""
        return self

    def __next__(self):
        """Return the next item in the sequence.

        Raises a StopIteration if there are no more items.
        """
        # add your code below


def test():
    """Run basic test cases for Range."""
    range1 = Range(1, 1)
    assert not range1
    range2 = Range(1, 5)
    assert len(range2) == 4
    range3 = Range(1, 5, 3)
    assert len(range3) == 2
    assert 1 in range3
    assert 4 in range3
    assert 3 not in range3
    assert 7 not in range3
    items = []
    for i in Range(-3, 11, 3):
        items.append(i)
    assert items == [-3, 0, 3, 6, 9]


if __name__ == '__main__':
    test()
