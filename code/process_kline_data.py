import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_home = 'data/'
symbol = 'BTCBUSD'

data_dir = data_home + symbol
load_dir = data_dir + '/raw_data/'
save_dir = data_dir + '/processed_data/1m.npy'

d = os.listdir(load_dir)
d.sort()
data_all = np.array([])

for file_name in d:
	file_path = load_dir + '/' + file_name
	df = pd.read_csv(file_path)
	data = df.to_numpy()
	data_all = np.vstack([data_all, data]) if data_all.size else data
	

 
np.save(save_dir, data_all)
