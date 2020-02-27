import numpy as np

# accumulate ---- 累积函数
def accumulate(np_arr):
	# 输入：arr = [a, b, c, d, e]
	# 输出：arr = [a, a+b, a+b+c, a+b+c+d, a+b+c+d+e]
	arr = []
	arr.append(np_arr[0])

	index = 1
	while index < len(np_arr):
		arr.append(np_arr[index] + arr[index - 1])
		index += 1
	return np.array(arr)

# 每天定量投
# average ---- 输出日平均成本曲线
# 定投状态的平均成本
# np_arr为每天的收盘价, aver_money为定投金额
def average(np_arr, aver_money):
	print("\n******************傻瓜式定投******************")
	print("截至今天，收盘价为：", np_arr[-1])
	days = len(np_arr)
	print("截至今天，本金合计：", days * aver_money)
	# 成本
	money_everyday = np.full(days, aver_money)
	money_accumulate = np.arange(aver_money, (days + 1) * aver_money, aver_money)
	# 持有份额
	num_everyday = money_everyday / np_arr
	num_accumulate = accumulate(num_everyday)

	# 平均成本
	money_average = money_accumulate / num_accumulate
	print("截至今天，成本价为：", money_average[-1])
	print("持有份额： ", num_accumulate[-1])
	print("当前价值： ", num_accumulate[-1] * np_arr[-1], "\n")
	print("收益率：", (num_accumulate[-1] * np_arr[-1] / money_accumulate[-1] - 1) * 100, "%")
	return money_average
	


# 线性权重定投
# weight_line_money ---- 通过线性权重计算出每天定投金额函数
# weight_donw_money ---- 通过逢低计算出每天定投的金额
# average_weight ---- 计算权重下的基金定投日平均成本曲线

# 线性权重判定函数	
def weight_line_money(np_arr, aver_money, weight):
		
	money_everyday = []
	money_everyday.append(aver_money)
	# print(money_everyday)
	for num in range(1, len(np_arr)):
		if np_arr[num] >= abs(weight):
			money_everyday.append(0)
		elif np_arr[num] <= (-abs(weight)):
			money_everyday.append(2 * aver_money)
		else:
			money = 2 * aver_money - \
					(2 * aver_money * np_arr[num] + 2 * aver_money * abs(weight)) \
					/ (2 * abs(weight))
			money_everyday.append(money)
	return np.array(money_everyday)

# 逢跌定投
def weight_down_money(np_arr, aver_money, weight):
	basic_money = 4 * aver_money
	money_everyday = []
	money_everyday.append(basic_money)
	
	for num in range(1, len(np_arr)):
		if np_arr[num] >= 0:
			money_everyday.append(0)
		# elif np_arr[num] <= (-abs(weight)):
		# 	money_everyday.append(2 * basic_money)
		else:
			money =  -2 * basic_money * np_arr[num] / weight
			money_everyday.append(money)
	return np.array(money_everyday)
	

# 设定权重的平均成本
# weight_method: line：线性权重
#				 down：逢跌投入
def average_weight(np_arr, aver_money, weight_method, weight = 0.03):

	print("\n******************权重式定投******************")
	print("截至今天，收盘价为：", np_arr[-1])
	days = len(np_arr)

	# 第一天为aver_money
	# 跌幅3%以上时加仓为：2*aver_money
	# 涨幅3%以上时加仓为：0
	np_arr_last_day = np.insert(np_arr, 0, 1, axis = 0)
	np_arr_last_day = np.delete(np_arr_last_day, -1, axis = 0)
	
	weight_arr = np_arr / np_arr_last_day - 1	

	# weight_method in ["line", "down"]
	if weight_method == "line":
		money_everyday = weight_line_money(weight_arr, aver_money, weight)
	
	elif weight_method == "down":
		money_everyday = weight_down_money(weight_arr, aver_money, weight)
	
	else:
		print("Weight method can only be 'line' and 'down'")
		raise NameError

	# print("everyday money:",money_everyday)
	money_accumulate = accumulate(money_everyday)
	print("截至今天，本金合计：", money_accumulate[-1])
	# 持有份额
	num_everyday = money_everyday / np_arr
	num_accumulate = accumulate(num_everyday)

	# 平均成本
	money_average = money_accumulate / num_accumulate
	print("截至今天，成本价为：", money_average[-1])
	print("持有份额： ", num_accumulate[-1])
	print("当前价值： ", num_accumulate[-1] * np_arr[-1])
	print("收益率：", (num_accumulate[-1] * np_arr[-1] / money_accumulate[-1] - 1) * 100, "%")
	return money_average
