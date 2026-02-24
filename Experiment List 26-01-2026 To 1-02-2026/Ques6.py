#Given an array of intervals where intervals[i] = [starti, endi], merge all
#overlapping intervals, and return an array of the non-overlapping intervals that
#cover all the intervals in the input.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # 1. Sort by the start time of each interval
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If 'merged' is empty or no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap exists: Merge by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
