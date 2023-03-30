import tkinter as tk
from tkinter import filedialog
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
import backtrader as bt

##################################
#          程序GUI窗口主体         #
##################################

class mainWindow():

 filePath=" "
 buy=0
 sell=0
 start=''
 end=''
 result=''

 cash=0   #本金
 percent=0 #float

 # 初始化的参数

 def __init__(self):

     self.inputCash=0
     self.inputBuy=0
     self.inputSell=0
     self.inputPercent=0.0
     self.startDate='Start Date'
     self.endDate='End Date'
     # 初始化传值的输入框和日期控件便于其他函数调用


     #回测算法初始化
     self.mainWin=tk.Tk()#创建主窗体
     self.setMainWin()


 def setMainWin(self):

    mainWin = self.mainWin #配置主窗体
    mainWin.title("数据回测")
    mainWin.geometry("350x600+750+150") #长600宽350 x=750 y=150
    stockCode=tk.Label(mainWin,text="股票代码:1865",font=('宋体',15,'bold italic'),
                            height=2,width=15)
    skillIndex=tk.Label(mainWin,text="技术指标:e.g.SMA",font=('宋体',15,'bold italic'),
                       height=2,width=18)

    # 固定信息
    labelStartTime=tk.Label(mainWin,text="起始时间:",font=('宋体',15,'bold italic'),
                   height=2,width=10)

    labelEndTime=tk.Label(mainWin,text="终止时间:",font=('宋体',15,'bold italic'),
                          height=2,width=10)

    labelBuy=tk.Label(mainWin,text="买入的MA线：",font=('宋体',15,'bold italic'),
                       height=2,width=12)

    labelSell=tk.Label(mainWin,text="沽出的MA线：",font=('宋体',15,'bold italic'),
                       height=2,width=12)
    labelCash=tk.Label(mainWin,text="投入本金的金额:",font=('宋体',15,'bold italic'),
                   height=2,width=15)
    labelCashPercent=tk.Label(mainWin,text="单笔投入占比：",font=('宋体',15,'bold italic'),
                       height=2,width=13)

    marketValueLabel=tk.Label(mainWin,text="最终市值：",font=('宋体',15,'bold italic'),
                         height=2,width=15)
    marketValue=tk.Label(mainWin,text="？？？",font=('宋体',15,'bold italic'),
                    width=8)

    inputCash=tk.Entry(mainWin)
    inputBuy=tk.Entry(mainWin)
    inputSell=tk.Entry(mainWin)
    inputPercent=tk.Entry(mainWin)
    # 输入框初始化


    stockCode.pack()
    skillIndex.pack()
    labelStartTime.pack(anchor='w')
    labelEndTime.pack(anchor='w')
    labelCash.pack(anchor='w')
    labelBuy.pack(anchor='w')
    labelSell.pack(anchor='w')
    labelCashPercent.pack(anchor='w')
    marketValueLabel.place(y=480)
    marketValue.place(x=150,y=490)
    #label装配
    inputCash.place(x=170,y=200)
    inputBuy.place(x=130,y=245)
    inputSell.place(x=130,y=290)
    inputPercent.place(x=140,y=335)
    # entry输入框装配位置参数


    buttpmSelectFile=tk.Button(mainWin,text="选择读取的数据文件",command=lambda : self.getFile(self.selectFile(mainWin=mainWin)))
    buttonOK=tk.Button(mainWin, text="     运行     ", command=lambda :self.showAndExcuteResult(
        inputBuy=inputBuy,inputSell=inputSell,inputPercent=inputPercent,inputCash=inputCash,result=marketValue))
    # 按钮绑定事件函数

    buttpmSelectFile.place(x=120,y=380)
    buttonOK.place(x=120,y=550)
    # 按钮位置装配

    self.setCalendorWidge()
    #日历控件绘制

    mainWin.mainloop()
    # 主窗体循环


 def setCalendorWidge(self):
     nowTime=datetime.now()
     calStart= DateEntry(self.mainWin, width=12, background='darkblue',foreground='white', borderwidth=2,maxdate=nowTime)
     calStart.place(x=120,y=100)

     calEnd= DateEntry(self.mainWin, width=12, background='darkblue',foreground='white', borderwidth=2,maxdate=nowTime)
     calEnd.place(x=120,y=150)

     self.start=calStart
     self.end=calEnd


 #日历控件初始化


 def returnDate(self,get):
     return get

 #

 def selectFile(self, mainWin):
    filePath=filedialog.askopenfile()
    if(filePath!=None):
     # print(filePath.name)
     filename=filePath.name
     result=tk.Label(mainWin,text=filename)
     result.place(x=10,y=420)

     return filename
 #选中资源文件


 def getFile(self,filePath):
      self.filePath=filePath
      print("设置的文件名",self.filePath)
 # 获取文件字符串

 def marketValue(self,F,data,SingleSmaStrategy):
     cerebro = bt.Cerebro()
     cerebro.adddata(data)
     cerebro.addstrategy(SingleSmaStrategy)
     cerebro.broker.setcash(F)  # 本金
     cerebro.run()
     print(f"最终市值为:{cerebro.broker.getvalue()}")

#市值算法计算

 def showAndExcuteResult(self,inputBuy,inputSell,inputPercent,inputCash,result):

    if(self.checkDataIsValid(inputBuy=inputBuy,inputSell=inputSell,inputPercent=inputPercent,inputCash=inputCash)):
        self.buy=int(inputBuy.get())
        self.sell=int(inputSell.get())
        self.cash=int(inputCash.get())
        self.percent=float(inputPercent.get())
        self.result=result.config(text=5000)
        self.startDate=datetime.strptime(str(self.start.get_date()),"%Y-%m-%d")
        self.endDate=datetime.strptime(str(self.end.get_date()),"%Y-%m-%d") #将用户输入的datetime保存到类属性
        print("运行调用文件名",self.filePath)
        print("买入ma",self.buy)
        print("沽出ma",self.sell)
        print("单笔占比",self.percent)
        print("本金",self.cash)
        print("起始日期",self.startDate)
        print("终止日期",self.endDate)
        print("市值",self.result)
    else:
        print("所有类内全局参数没有变化，因为输入有误")
 # 统一返回输入框信息并写入对象属性作为算法读取的参数

 def checkDataIsValid(self,inputBuy,inputSell,inputPercent,inputCash):
    checkDate=bool((datetime.strptime(str(self.start.get_date()),"%Y-%m-%d")<datetime.strptime(str(self.end.get_date()),"%Y-%m-%d")))#检验用户日期输入是否正确，转为bool类型
    checkFile=not(self.filePath.isspace())
    print("是否有文件",checkFile)
    if (checkFile&inputBuy.get().isdigit()&inputSell.get().isdigit()&inputPercent.get().isdigit()&inputCash.get().isdigit()&checkDate):
        return True
    else:
        messagebox.showerror("出错了捏~","请检查输入格式是否正确！\n\n"
                                               "输入格式应符合：\n"
                                               "1.所有输入框不为空且必须全为整数类型\n"
                                               "2.起始日期应小于终止日期\n"
                                               "3.选择读取的数据文件不能为空")
        return False
#   验证 框内数字类型

##################################
#           回测算法封装           #
##################################

class SingleSmaStrategy(bt.Strategy):
    def __init__(self):

        self.simple_ma_buy = bt.indicators.SMA(self.datas[0].close, period=60)  # 60
        self.simple_ma_sell = bt.indicators.SMA(self.datas[0].close, period=20)  # 20

    def next(self,F,P):
        if not self.position.size:
            if self.datas[0].close[-1] < self.simple_ma[-1] and self.datas[0].close[0] > self.simple_ma[0]:
                self.buy(size=(F*P)/self.datas[0].close[0])
        elif self.datas[0].close[-1] > self.simple_ma2[-1] and self.datas[0].close[0] < self.simple_ma2[0]:
            self.sell(size=(F*P)/self.datas[0].close[0])




if __name__=='__main__':

 mystrategy=SingleSmaStrategy()
 mywin=mainWindow()
 # cerebro = bt.Cerebro()
 # cerebro.adddata()
 # cerebro.addstrategy(SingleSmaStrategy)
 # cerebro.broker.setcash(mywin.cash)  # 本金
 # cerebro.run()
 # print(f"最终市值为:{cerebro.broker.getvalue()}")



