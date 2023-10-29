import numpy as np
import datetime
import time

from binance.spot import Spot

api_endpoint = 'https://api.binance.us'
symbol = 'BNBUSDT'

start_year = 2021
start_month = 4
start_day = 1

end_year = 2021
end_month = 4
end_day = 2

interval_code = '1m'
interval_ms = 1000*60

start_datetime = datetime.datetime(start_year, start_month, start_day)
start_timestamp = time.mktime(start_datetime.timetuple()) * 1000 # In milliseconds 
start_timestamp = int(start_timestamp) 

end_datetime = datetime.datetime(end_year, end_month, end_day)
end_timestamp = time.mktime(end_datetime.timetuple())

# end_timestamp = int(end_timestamp)
end_timestamp = start_timestamp + interval_ms * 435

client = Spot(base_url=api_endpoint)

# Get last 10 klines of BNBUSDT at 1h interval
k_line_data = client.klines(symbol, interval_code, startTime=start_timestamp, endTime=end_timestamp, limit=10)
k_line_data = np.array(k_line_data)
print(k_line_data)
k_line_data = client.klines(symbol, interval_code, startTime=start_timestamp, endTime=end_timestamp, limit=10)
k_line_data = np.array(k_line_data)
print(k_line_data)


