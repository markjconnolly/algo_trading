import numpy as np
import datetime
import time
import sqlite3

class realtime_source:

    def __init__(self) -> None:
        self.last_update = 0

    def get_data(self, symbol):
        sql_check_spec = '''SELECT ticker_time, open_price, volume FROM spot_entry WHERE symbol = ? and ticker_time > ? and ticker_time < ?'''