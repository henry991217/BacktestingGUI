from datetime import datetime
import backtrader as bt

class SingleSmaStrategy(bt.Strategy):
  def __init__(self):
    self.simple_ma = bt.indicators.SMA(self.datas[0].close,period=NUM)
    self.simple_ma2 = bt.indicators.SMA(self.datas[0].close,period=NUM2)
  def next(self):
    if not self.position.size:
      if self.datas[0].close[-1] < self.simple_ma[-1] and self.datas[0].close[0] > self.simple_ma[0]:
        self.buy(size=(F*S)/self.datas[0].close[0])
    elif self.datas[0].close[-1] > self.simple_ma2[-1] and self.datas[0].close[0] < self.simple_ma2[0]:
      self.sell(size=(F*S)/self.datas[0].close[0])

datapath = "E:/2.csv"

data = bt.feeds.GenericCSVData(dataname=datapath,datetime=0,open=1,high=2,low=3,close=4,volume=5,openinterest=-1,dtformat=("%Y%m%d"),fromdate=datetime(2010,1,1),todate=datetime(2023,3,22))


NUM=int(input("请输入买入的MA线："))
NUM2=int(input("请输入沽出的MA线："))
S=float(input("请输入单笔投入的占比："))
F=int(input("请输入投入本金的金额："))
cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(SingleSmaStrategy)
cerebro.broker.setcash(F)
cerebro.run()
print(f"最终市值为:{cerebro.broker.getvalue()}")
