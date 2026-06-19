"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    
    def overlaps(self, first_interval, second_interval):
        return ((first_interval.end > second_interval.start and first_interval.start <= second_interval.start)
        or (first_interval.start < second_interval.end and first_interval.end >= second_interval.end))

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i, interval in enumerate(intervals):
            for _, second_interval in enumerate(intervals[i + 1:]):
                if self.overlaps(interval, second_interval):
                    print(f"Intervals {interval} and {second_interval} overlap!")
                    return False
        return True

