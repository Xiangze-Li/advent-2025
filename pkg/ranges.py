from typing import Protocol
import bisect


class Ordered(Protocol):
    """Protocol for types that support ordering operations."""

    def __le__(self, other, /) -> bool: ...
    def __lt__(self, other, /) -> bool: ...
    def __ge__(self, other, /) -> bool: ...
    def __gt__(self, other, /) -> bool: ...


class Ranges[T: Ordered]:
    """
    Ranges is a collection of non-overlapping inclusive ranges.

    Each range is represented by a `tuple[T, T]` of [lower_bound, upper_bound].
    For `i`, `j` in Ranges such that `i < j`, it guarantees `Ranges[i][1] < Ranges[j][0]`.
    """

    def __init__(self, ranges: list[tuple[T, T]] = []):
        for i in ranges:
            if not i[0] <= i[1]:
                raise ValueError(f"Invalid range: [{i[0]}, {i[1]}]")
        ranges.sort()
        self.ranges = ranges.copy()

    def __len__(self):
        return len(self.ranges)

    def __getitem__(self, idx: int) -> tuple[T, T]:
        return self.ranges[idx]

    def __delitem__(self, idx: int) -> None:
        del self.ranges[idx]

    def __iter__(self):
        return iter(self.ranges)

    def __contains__(self, item: tuple[T, T]) -> bool:
        if not item[0] <= item[1]:
            raise ValueError(f"Invalid range: [{item[0]}, {item[1]}]")
        idx = bisect.bisect_right(self.ranges, item)
        if idx > 0:
            left = self[idx - 1]
            if left[0] <= item[0] and item[1] <= left[1]:
                return True
        if idx < len(self.ranges):
            right = self[idx]
            if right[0] <= item[0] and item[1] <= right[1]:
                return True
        return False

    def add(self, range: tuple[T, T]) -> None:
        """
        add adds a new range, merging overlapping ranges to keep invariants.

        :param range: The range to add
        :type range: tuple[T, T]
        """
        if not range[0] <= range[1]:
            raise ValueError(f"Invalid range: [{range[0]}, {range[1]}]")

        idx = bisect.bisect_right(self.ranges, range)
        if idx > 0:
            left = self[idx - 1]
            if left[1] >= range[0]:
                left = (left[0], max(left[1], range[1]))
                self.ranges[idx - 1] = left
                idx -= 1
            else:
                self.ranges.insert(idx, range)
                left = range
        else:
            self.ranges.insert(0, range)
            left = range

        idx_right = idx + 1
        while idx_right < len(self.ranges) and left[1] >= self[idx_right][1]:
            idx_right += 1
        del self.ranges[idx + 1 : idx_right]

        if idx + 1 < len(self.ranges):
            right = self.ranges[idx + 1]
            if left[1] >= right[0]:
                self.ranges[idx] = (left[0], max(left[1], right[1]))
                del self.ranges[idx + 1]

    def check(self, val: T) -> bool:
        """
        check determines if `val` falls within any range.

        :param val: The value to check
        :type val: T
        :return: True if `val` is within any range, False otherwise
        :rtype: bool
        """
        return self.find(val) is not None

    def find(self, val: T) -> tuple[T, T] | None:
        """
        find returns the range that contains `val`, or None if not found.

        :param val: The value to find
        :type val: T
        :return: The range containing `val`, or None
        :rtype: tuple[T, T] | None
        """
        idx = bisect.bisect_right(self.ranges, (val, val))

        if idx > 0:
            if self[idx - 1][1] >= val:
                return self[idx - 1]

        if idx < len(self.ranges):
            if self[idx][0] <= val:
                return self[idx]

        return None
