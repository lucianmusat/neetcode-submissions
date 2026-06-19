"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        meeting_points = []
        min_days = 0
        # Create meeting points, stamped with 1 for meeting starts, and -1 for meeting ends
        for interval in intervals:
            meeting_points.append((interval.start, 1))
            meeting_points.append((interval.end, -1))

        # Sort the points, making sure in case of start-end overlap to put the end first
        # so we don't count the meeting room twice
        meeting_points.sort(key=lambda x: (x[0], x[1]))

        current_meetings = 0
        for time, point_type in meeting_points:
            current_meetings += point_type
            min_days = max(current_meetings, min_days)

        return min_days