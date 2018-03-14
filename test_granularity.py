from datetime import datetime, timedelta
from granularity import Granularity, TimeFrame
import unittest

class TestTimeFrame(unittest.TestCase):
    
    def test_get_timeframes(self):
        start = datetime(2018, 1, 1)
        end = datetime(2018, 1, 10)
        gran = Granularity.MINUTES_15

        timeframes = TimeFrame.get_timeframes(start, end, gran)
        self.assertEqual(len(timeframes), 3)

        start = datetime(2018, 1, 1)
        end = datetime(2018, 1, 10)
        gran = Granularity.MINUTES_1

        timeframes = TimeFrame.get_timeframes(start, end, gran)
        self.assertEqual(len(timeframes), 43)

    if __name__ == '__main__':
        unittest.main()