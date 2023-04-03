import pandas as pd
import tushare as ts
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
ts.set_token('b30b7e60a28b12ee3d130896e350bdaaccc38e5902cf8b129b85b0e3')
pro = ts.pro_api()

def load_stock(code,start,end,output_file):
    try:
        df = pd.read_csv(output_file)
        print('载入股票数据文件完毕')
    except FileNotFoundError:
        print('文件未找到，重新下载中')
        df = pro.daily(ts_code=code,autype='qfq',start_date=start,end_date=end)
        df.index = pd.to_datetime(df.trade_date)
        df = df[['open','high','low','close','vol']]
        df.to_csv(output_file)
        print('下载完成')
    return df
def acquire_code():
    inp_code = input("请输入股票代码[以.SH为后缀]:")
    inp_start = input("请输入开始时间:")
    inp_end = input("请输入结束时间:")
    inp_output_file = input("文件名:")
    df = load_stock(inp_code,inp_start,inp_end,inp_output_file)
    df.sort_index(inplace=True)
   