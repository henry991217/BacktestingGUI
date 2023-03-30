from datetime import datetime
import backtrader as bt


F = 1000000.00

class SingleSmaStrategy(bt.Strategy):
    def __init__(self,buy,sell):
        self.buy=buy
        self.sell=sell
        self.simple_ma_buy = bt.indicators.SMA(self.datas[0].close, period=60)  # 60
        self.simple_ma_sell = bt.indicators.SMA(self.datas[0].close, period=20)  # 20

    def next(self,F,P):
        if not self.position.size:
         if self.datas[0].close[-1] < self.simple_ma[-1] and self.datas[0].close[0] > self.simple_ma[0]:
            self.buy(size=(F*P)/self.datas[0].close[0])
        elif self.datas[0].close[-1] > self.simple_ma2[-1] and self.datas[0].close[0] < self.simple_ma2[0]:
            self.sell(size=(F*P)/self.datas[0].close[0])


datapath = "E:/2.csv"


data = bt.feeds.GenericCSVData(dataname=datapath, datetime=0, open=1, high=2, low=3, close=4, volume=5, openinterest=-1,
                               dtformat=("%Y%m%d"), fromdate=datetime(2010, 1, 5), todate=datetime(2020, 1, 20))



s=SingleSmaStrategy(buy=60,sell=20)

print(s)

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(s)
cerebro.broker.setcash(F)  # 本金
cerebro.run()
print(f"最终市值为:{cerebro.broker.getvalue()}")



