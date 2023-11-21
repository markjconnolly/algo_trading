import numpy as np
import datetime
import time
import sqlite3

from binance.spot import Spot

symbol = 'BTCUSDT'

api_endpoint = 'https://api.binance.us'
client = Spot(base_url=api_endpoint)

interval_code = '1m'
interval_ms = 1000*60*1000

connection = sqlite3.connect("/Users/mconn/precision_crypto/database/ticker_data.db")
with connection:
    cursor = connection.cursor()

sql_max_time_spec = '''SELECT MAX(ticker_time) FROM spot_entry WHERE symbol = ?'''
sql_check_spec = '''SELECT COUNT(*) FROM spot_entry WHERE symbol = ? and ticker_time = ?'''
sql_insert_spec = '''INSERT INTO spot_entry(symbol, ticker_time, open_price, close_price, min_price, max_price, volume)
        VALUES(?, ?, ?, ?, ?, ?, ?)'''

sql_max_time_val = (symbol,)

# Get the current time
current_datetime = datetime.datetime.now()
current_timestamp = time.mktime(current_datetime.timetuple()) * 1000 # In milliseconds 
current_timestamp = int(current_timestamp)

# Start from the end of the current record
# Get the max time in the database for this symbol and calculate end time
sql_max_time_val = (symbol,)
cursor.execute(sql_max_time_spec, sql_max_time_val)
start_timestamp = cursor.fetchall()
start_timestamp = start_timestamp[0][0]

# Start from an arbitary date
# start_year = 2023
# start_month = 1
# start_day = 1

# start_datetime = datetime.datetime(start_year, start_month, start_day)
# start_timestamp = time.mktime(start_datetime.timetuple()) * 1000 # In milliseconds 
# start_timestamp = int(start_timestamp) 

end_timestamp = start_timestamp + interval_ms

while start_timestamp < current_timestamp:

    # Get k-line data in interval after max data
    k_line_data = client.klines(symbol, interval_code, startTime=start_timestamp, endTime=end_timestamp, limit=1000)
    k_line_data = np.array(k_line_data)
    
    # Iterate and add to database
    for k_line in k_line_data:   
        ticker_time = k_line[0]
        sql_check_val = (symbol,) + (ticker_time,)

        cursor.execute(sql_check_spec, sql_check_val)
        counts = cursor.fetchall()
        
        # Do not add if a row with this symbol and timestamp exists, 
        if not counts[0][0]:
            sql_insert_val = (symbol,) + tuple(k_line[[0, 1, 4, 3, 2, 5]])
            cursor.execute(sql_insert_spec, sql_insert_val)

    cursor.execute(sql_max_time_spec, sql_max_time_val)
    start_timestamp = cursor.fetchall()[0][0]
    end_timestamp = start_timestamp + interval_ms
    connection.commit()

    # time.sleep(1)

cursor.close()




