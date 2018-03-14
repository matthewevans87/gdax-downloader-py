from enum import IntEnum
from datetime import datetime, timedelta
import unittest

class Granularity(IntEnum):
    MINUTES_1 = 60
    MINUTES_5 = 300
    MINUTES_15 = 900
    HOURS_1 = 3600 
    HOURS_6 = 21600 
    HOURS_24 = 86400

class TimeFrame:

    MaxResults = 300

    def __init__(self, start:datetime, end:datetime, granularity:Granularity):
        self.start = start
        self.end = end
        self.granularity = granularity

    def __str__(self):
        return "start: {start}, end: {end}, gran:{gran}".format(start=self.start, end=self.end, gran=self.granularity.name)

    @staticmethod
    def get_timeframes(start:datetime, end:datetime, granularity:Granularity) -> list:
        s = start
        e = min( (start + timedelta(seconds=(granularity * TimeFrame.MaxResults))), end )

        timeframes = []

        while s < end:
            timeframes.append(TimeFrame(s, e, granularity))
            
            s = datetime.fromtimestamp(e.timestamp())
            e = min( (e + timedelta(seconds=(granularity * TimeFrame.MaxResults))), end )

        return timeframes



