import numpy as np
import matplotlib.pyplot as plt

from get_stock_datas import random_market
# money = 1000
# weight = 2
# x = np.arange(-0.03, 0.031, 0.001)
# y = money - 2 * money / 0.06 * x
# plt.plot(x, y, color = "blue")
# low = np.arange(-0.04, -0.03, 0.001)
# high = np.arange(0.03, 0.04, 0.001)

# value_0 = np.full(11, 0)
# value_2000 = np.full(11, 2000)

# plt.plot(low, value_2000, color = "blue")
# plt.plot(high, value_0, color = "blue")
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))


# plt.show()



data = random_market()
x = [x[0] for x in data]
y = [x[1] for x in data]
plt.plot(x, y)
plt.show()