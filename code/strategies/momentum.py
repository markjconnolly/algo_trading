
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import sqlite3

class momentum:

    # This will need to initialize (and store) its state from a database
    def __init__(self, momentum_window, holdings, symbol):
        self.momentum_window = momentum_window
        self.holdings = holdings
        self.last_update_time = 0
        self.symbol = symbol
        
    def run_algo(self):
        sql_time_spec = '''SELECT MAX(ticker_time) FROM spot_entry WHERE symbol = ?'''
        sql_check_spec = '''SELECT ticker_time, open_price, volume FROM spot_entry WHERE symbol = ? and ticker_time > ? and ticker_time < ?'''

        sql_time_val = ('BTCUSDT',)
        connection = sqlite3.connect("database/ticker_data.db")
        with connection:
            cursor = connection.cursor()

        cursor.execute(sql_time_spec, sql_time_val)
        latest_time_db = np.array(cursor.fetchall())

        if latest_time_db > self.last_update_time:
            calculated_timestamp = latest_time_db - self.momentum_window
            start_timestamp = calculated_timestamp - 10*1000
            end_timestamp = calculated_timestamp - 10*1000

            sql_check_val = (self.symbol,) + (start_timestamp,) + (end_timestamp,)
            cursor.execute(sql_check_spec, sql_check_val)
            
            spot_data = cursor.fetchall()
            spot_data = np.array(spot_data)


        # Get data
        # 
        # Calculate metric
        #  
        # Make trade
        # 
        # Update state

        
        
m1 = momentum(60*24*7, 100)
m1.run_algo()
    

