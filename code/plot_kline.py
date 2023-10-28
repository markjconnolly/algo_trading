import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time

slow_window = 1*24*60
risk_factor = 0.8

# 
data_home = 'data/'
symbol = 'BTCBUSD'

data_dir = data_home + symbol
load_path = data_dir + '/processed_data/1m.npy'


# 
start_year = 2021
start_month = 4
start_day = 1

start_datetime = datetime.datetime(start_year, start_month, start_day)
start_timestamp = time.mktime(start_datetime.timetuple())
start_timestamp = np.array(start_timestamp)

end_year = 2022
end_month = 4
end_day = 1

end_datetime = datetime.datetime(end_year, end_month, end_day)
end_timestamp = time.mktime(end_datetime.timetuple())

# [0] - time, [1] - min, [2] - max, [3] - open, [4] - close, [5] - volume
kline_data = np.load(load_path)
t = kline_data[:,0]/1000

start_index = np.where(t == start_timestamp)[0][0]
end_index = np.where(t == end_timestamp)[0][0]
n_points = end_index - start_index

open_price = kline_data[start_index:end_index,3]
volume = kline_data[start_index:end_index,5]

t = t[start_index:end_index]

fast_mean = np.array([0,0])
slow_mean = np.array([0,0])

usd = 100
usd_balance = np.array([usd])

btc = 0
btc_hold = usd / open_price[slow_window]
purchase_price = 0

usd_balance_hold = np.array([usd])

n_trades = 0
t_trade = np.array(t[slow_window])

for current_index in range(slow_window, n_points, 60):
	
	current_price = open_price[current_index]

	segment_start_idx = current_index - slow_window
	
	open_segment = open_price[segment_start_idx:current_index]
	open_mean = np.mean(open_segment)

	volume_segment = volume[segment_start_idx:current_index]
	volume_mean = np.mean(volume_segment)

	if usd:
		if current_price < open_mean and volume[current_index] > volume_mean:
		
			btc = usd / open_price[current_index]
			usd = 0
			print('Buy')

	if btc:
		current_price = open_price[current_index]

		# if purchase_price and current_price < purchase_price * risk_factor:
		# 	usd = btc * open_price[current_index]
		# 	btc = 0

		# 	t_trade = np.append(t_trade, t[current_index])
		# 	usd_balance = np.append(usd_balance, usd)
		# 	usd_balance_hold = np.append(usd_balance_hold, usd_hold)

		# 	print('STOP LOSS')

		if open_price[current_index] > open_mean and volume[current_index] < volume_mean:
		
			usd  = btc * open_price[current_index]
			usd_hold = btc_hold * open_price[current_index]
			btc = 0

			purchase_price = open_price[current_index]
			n_trades += 1

			t_trade = np.append(t_trade, t[current_index])
			usd_balance = np.append(usd_balance, usd)
			usd_balance_hold = np.append(usd_balance_hold, usd_hold)

			print('{}:Sell'.format(n_trades))

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(t-t[0],open_price,color='black')
# ax1.plot(t[slow_window:]-t[0], fast_mean)
# ax1.plot(t[slow_window:]-t[0], slow_mean)

ax2.plot(t_trade-t[0], usd_balance)
ax2.plot(t_trade-t[0], usd_balance_hold)

plt.show()




































