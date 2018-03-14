#GDAX Downloader
import gdax
import datetime
import time
from granularity import Granularity, TimeFrame

productIds = [
            # 'BCH-BTC',
            'BCH-USD',
            'BTC-EUR',
            'BTC-GBP',
            'BTC-USD',
            'ETH-BTC',
            'ETH-EUR',
            'ETH-USD',
            'LTC-BTC',
            'LTC-EUR',
            'LTC-USD',
            'BCH-EUR'
        ]

        

public_client = gdax.PublicClient()

end = datetime.datetime(2018, 1, 3)
start = datetime.datetime(2018, 1, 1)
timeframes = TimeFrame.get_timeframes(start, end, Granularity.MINUTES_1)

historicRates = []
for t in timeframes:
    print(t)
    results = public_client.get_product_historic_rates("btc-usd", start = t.start, end = t.end, granularity = t.granularity.value)
    print("{len} result(s)".format(len = len(results)))
    historicRates.extend(results)
    time.sleep(1)

print(len(historicRates))
print(historicRates)