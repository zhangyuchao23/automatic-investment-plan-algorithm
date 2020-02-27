import json
import requests
import os
import numpy as np
import matplotlib.pyplot as plt

stock_data = "E:\\pythonLife\\other_item\\automatic_investment_plan(AIP)\\stock_datas\\"

# 从文件中直接读取数据
def read_txt():

    file = open(stock_data + "data_file.txt")
    data = file.read()
    file.close()
    data = data[2:-2]
    data_list = data.split("], [")
    
    data = []
    for element in data_list:
        data_temp = element.split(",")
        
        # batch transfer str to float
        data_int_temp = map(eval, data_temp)
        data_list_temp = list(data_int_temp)
        # print(data_list_temp)
        data.append(data_list_temp)

    return data



# 爬取网络上的数据
def download_data():
    
    if not os.path.exists(stock_data):
        os.makedirs(stock_data)

    url='http://yunhq.sse.com.cn:32041/v1/sh1/dayk/000001?callback=jQuery111208282462776376776_1569062885488&select=date%2Copen%2Chigh%2Clow%2Cclose%2Cvolume&begin=-300&end=-1&_=1569062885522' 
    response=requests.get(url,headers={'Referer': 'http://www.sse.com.cn/market/price/trends/'})
    json_str=response.text[42:-1]

    data=json.loads(json_str)

    # 进入到数据文件夹
    os.chdir(stock_data)
    
    # 保存数据
    data_file = open("data_file.txt", "w", encoding = "utf-8")
    data_file.write(str(data["kline"]))
    data_file.close()    
    
    return data['kline'] 


# 生成随机市场
def random_market():
    x = 0
    y = 2000
    data = [[0, 2000.00]]
    for day in range(10000):
        x += 1

        if x > 5:
            if data[x - 1] > data[x - 2] > data[x - 3] > data[x - 4]:
                y = np.random.uniform(0.9 * y, y)
                continue
            elif data[x - 1] < data[x - 2] < data[x - 3] < data[x - 4]:
                y = np.random.uniform(y, 1.1 * y)
                continue

        y = np.random.uniform(y * 0.95, y * 1.05)
        data.append([x, y])
    return data
     