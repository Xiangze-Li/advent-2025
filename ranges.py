import bisect


class Ranges:
    def __init__(self, ranges: list[tuple[int, int]] = []):
        self.ranges = ranges

    def __iter__(self):
        return iter(self.ranges)

    def add(self, range: tuple[int, int]) -> None:
        idx = bisect.bisect_right(self.ranges, range)
        if idx > 0:
            left = self.ranges[idx - 1]
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

        if idx < len(self.ranges) - 1:
            right = self.ranges[idx + 1]
            if left[1] >= right[0]:
                merged = (left[0], max(left[1], right[1]))
                self.ranges[idx] = merged
                del self.ranges[idx + 1]

    def check(self, val: int) -> bool:
        idx = bisect.bisect_right(self.ranges, (val, val))

        if idx > 0:
            if self.ranges[idx - 1][1] >= val:
                return True

        if idx < len(self.ranges):
            if self.ranges[idx][0] <= val:
                return True

        return False
