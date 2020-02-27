import os
import numpy as np
import matplotlib.pyplot as plt

from get_stock_datas import read_txt, download_data
from function import average, average_weight


def show():

	try:
		data = np.array(read_txt())
	except FileNotFoundError:
		data = np.array(download_data())
	

	days = [x[0] for x in data]
	print("定投时间为： ", len(days))
	arr_current = [x[4] for x in data]

	average_money1 = average(arr_current[:], 1000)
	average_money2 = average_weight(arr_current[:], 1000, weight_method = "line", weight = 0.03)
	average_money3 = average_weight(arr_current[:], 1000, weight_method = "down", weight = 0.03)
	# print(average_money)
	index = range(len(days))
	limit = 90
	plt.xticks(index[::limit], days[::limit])
	plt.plot(index[:], arr_current[:], color = "black")
	# plt.plot(index[:], average_money1[:], color = "blue")
	plt.plot(index[:], average_money2[:], color = "red")
	plt.plot(index[:], average_money3[:], color = "green")
	plt.show()

if __name__ == "__main__":
	show()
	
